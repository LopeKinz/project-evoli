import os
import subprocess


def get_hwid():
    if os.name == "nt":
        return (
            subprocess.check_output("wmic csproduct get uuid")
            .decode()
            .split("\n")[1]
            .strip()
        )
    else:
        return "Error while getting Windows HWID"
