import mss
import cv2 as cv
import numpy
import pyautogui
import globals

# Comparison coefficient, 0.9 is 90% of relevance
CV_COEFF = 0.9

# Should use just one thread for openCV processing, maybe more stable
cv.setNumThreads(0)

# initialize global variables
globals.initialize()

# Read screen width and height, save to global vars
globals.width, globals.height = pyautogui.size()

# Part of the screen to capture
monitor = {"top": 0, "left": 0, "width": globals.width, "height": globals.height}


##################### Image recognition ################################


def screenshot():
    # Capture the screen
    with mss.mss() as sct:
        template = numpy.array(sct.grab(monitor))

    # Convert captured for usage with openCV
    template = cv.cvtColor(template, cv.COLOR_RGBA2RGB)

    # If you want to check what part of the screen is captured, uncomment the line below
    # cv.imwrite('template.png', template)

    return template


def image_check(file, passedTemplate):
    # Read comparison image
    img = cv.imread(file, cv.IMREAD_COLOR)

    # If you want to check how the comparison image looks, uncomment the line below
    # cv.imwrite('template_square.png', img)

    # Match captured image with comparison image
    res = cv.matchTemplate(img, passedTemplate, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if globals.debug:
        print(file, "max_val, max_loc:", max_val, max_loc)
    return max_val, max_loc


def find_image(passedTemplate):
    # Save relevance value and location of the comparison image
    max_val, max_loc = image_check("files/comparison_image.png", passedTemplate)

    if max_val > CV_COEFF:
        return max_loc
    else:
        return False


####################### Keyboard control ###############################


# Listen for keyboard input to toggle debug with Page Up/Down
def key_press(key):
    try:
        if key.name.lower() == "page up":
            globals.debug = True
            print("----------------Debug started----------------")
        elif key.name.lower() == "page down":
            globals.debug = False
            print("----------------Debug stopped----------------")
    except Exception as e:
        print(e)


######################### Write errors in log ############################


def log(txt):
    with open("debug.log", "a+") as log_file:
        log_file.write(txt)
        log_file.write("\n")
