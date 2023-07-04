import ctypes


def kill_bios():
  if ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.kernel32.SetSystemTime(None, None)
  else:
    print("Error")
