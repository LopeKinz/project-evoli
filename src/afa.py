import ctypes
import sys


class AdminRightsChecker:

    @staticmethod
    def check() -> str:
        
        """
        Asks for admin.

        Returns:
            str: "Already Admin" if the user has administrator rights, or "Asked For Admin" if it asked for admin duh.
        """
        
        if ctypes.windll.shell32.IsUserAnAdmin():
            return "Already Admin"
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return "Asked For Admin"

# test case 

if __name__ == "__main__":
    main = AdminRightsChecker()
    result = main.check()
    print(result)
