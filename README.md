# OpenCV test - automatic Whac-a-mole

In this little project I tried to use Python and openCV template matching to play Whac-a-mole automatically while holding the Spacebar key.

If you want to try it, you will either need [Python Poetry (package manager)](https://python-poetry.org/docs/) or manually install needed packages:
+ Python 3.11
+ keyboard
+ opencv-python-headless
+ mss
+ pyautogui

How to run with Poetry:
1. Clone the repo
2. [Install Poetry](https://python-poetry.org/docs/)
3. Run `poetry install` from terminal while positioned in the project folder
4. Open [Whac-a-mole](https://www.kennyyipcoding.com/whac-a-mole/)
5. Screenshot the part of image that you want to recognize (the mole in this example) that is always unchanged (example comparison_image.png included) and put it in `openCV_test/files` as _comparison_image.png_
6. Run _start.bat_ from `openCV_test/`
7. Hold Spacebar to automatically click on the mole and rack up points

Press _Page Up_ to see debug info in terminal, _Page Down_ to turn it off.

To stop the script, use _Ctrl+C_ or exit the terminal.