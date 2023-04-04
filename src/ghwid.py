import os, subprocess
def get_hwid():
    if os.name == 'nt':
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return hwid
    else:
        return("Error while getting Windows HWID")
