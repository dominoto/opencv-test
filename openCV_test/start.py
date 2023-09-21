import keyboard
import time
import pyautogui
import functions
import globals

# Modifiable delay in seconds
WANTED_DELAY = 0

# Capture keypress events
keyboard.on_press(functions.key_press)

print("Script started!")

if globals.debug:
    print("********************************************************")
    print("********************** DEBUG ***************************")

while True:
    while keyboard.is_pressed("space"):
        try:
            # Start performance timer
            tic = time.perf_counter()

            # Take screenshot and save in template for comparisons
            template = functions.screenshot()

            # Check image
            max_loc_or_False = functions.find_image(template)

            # End performance timer
            toc = time.perf_counter()

            # Change delay to zero if time to read the image takes more than wanted delay
            if (toc - tic) > WANTED_DELAY:
                globals.delay = 0
            else:
                globals.delay = WANTED_DELAY - (toc - tic)
            if globals.debug:
                print("Image found in ", toc - tic, " seconds")
                print("Delay: ", globals.delay)

            # Send a click if image is found
            if max_loc_or_False != False:
                time.sleep(globals.delay)
                pyautogui.click(max_loc_or_False)
                if globals.debug:
                    print("Whacked the mole!")
            else:
                if globals.debug:
                    print("No mole in sight!")

        except Exception as e:
            # Show errors
            print(e)

            # Write errors in log
            functions.log("Error in function: " + str(e))

    # Default delay so the infinite loop doesn't take up too much CPU cycles, in seconds
    time.sleep(0.01)
