import pyautogui
import time

try:
    time.sleep(3)
    while True:
        play = pyautogui.locateCenterOnScreen(r'play.png', confidence=0.8)
        if play is None:
            play2 = pyautogui.locateCenterOnScreen(r'play2.png', confidence=0.8)
            if play2 is None:
                time.sleep(60)
            else:
                pyautogui.click(play2)
                time.sleep(60)

        else:
            pyautogui.click(play)
            time.sleep(180)

        time.sleep(5)

except KeyboardInterrupt:
    print('Program end')
