import ctypes
import sys


class AFA:
    
    @staticmethod
    def check():
        if ctypes.windll.shell32.IsUserAnAdmin():
            return "Already Admin"
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return "Asked For Admin"


if __name__ == "__main__":
    main = AFA()
    result = main.check()
    print(result)
