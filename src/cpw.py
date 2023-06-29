import os, requests, ctypes
def change_pw(password):
  is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
  if !is_admin:
        return ("Not running as admin. Operation aborted")
  status = os.popen(r"net user %username% " + password).read()
  if "success" in status.lower():
        return (fr"Success: Password changed to {password}")
