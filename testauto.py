import pyautogui
import time

n=0
try:
    while True:
        pyautogui.moveTo(800,800)
        pyautogui.click()
        pyautogui.scroll(1000)
        time.sleep(2)
        pyautogui.scroll(1000)
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)
        pyautogui.scroll(1000)
        time.sleep(2)
        pyautogui.scroll(1000)
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)
        pyautogui.press('home')
        
        brave = pyautogui.locateCenterOnScreen(r'click.png', confidence=0.8)
        if brave is None:
            time.sleep(60)

        else:
            pyautogui.click(brave)
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            n+=1
            print(n)
            time.sleep(180)

        time.sleep(5)

except KeyboardInterrupt:
    print('Program end')
