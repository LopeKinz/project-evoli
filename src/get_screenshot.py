from string import ascii_letters, digits
import pyautogui
import os
import random
def get_screenshot():
    get_screenshot.scrn = pyautogui.screenshot()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    global scrn_path
    scrn_path= os.path.join(
        dir_path, f"Screenshot_{''.join(random.choices(list(ascii_letters + digits), k=5))}.png" # Avoiding overwriting / exception.
    )
    
    get_screenshot.scrn.save(scrn_path)
    return scrn_path
