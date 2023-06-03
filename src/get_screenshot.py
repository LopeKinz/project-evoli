import pyautogui
import os
from time import gmtime, strftime
import platform
def get_screenshot():
    get_screenshot.scrn = pyautogui.screenshot()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    date =  strftime("%H%M%S_%Y-%m-%d", gmtime())
    global scrn_path
    scrn_path= os.path.join(
        dir_path, f"Screenshot_{date}_{platform.node()}.png"
    )

    get_screenshot.scrn.save(scrn_path)
    return scrn_path
