import ctypes
def block():
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(True)
                return "Blocked"
            else:
                return "No Admin"
def unblock():
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(False)
                return "Unblocked"
            else:
                return "No Admin"
