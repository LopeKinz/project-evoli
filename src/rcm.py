import win32api
import win32con

def create_remote_message_box(computer_name, message, title):
    win32api.MessageBox(win32con.NULL, message, title, win32con.MB_OK | win32con.MB_ICONINFORMATION, 0, computer_name)


# Not DONE!
