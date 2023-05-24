import os
import random
import string
import subprocess
import sys
import threading
import time


def createaccsloop(accname):
    try:
        nums = string.digits
        new = "".join(random.choice(nums) for _ in range(5))
        print(f"{Fore.GREEN}Adding new user: {accname}{new}")
        subprocess.os.system(f"net user {accname}{new} {accname}{new} /add")
        print(f"{Fore.GREEN}Successfully added new user! User: {accname}{new}")
    except:
        print(f"{Fore.RED}Failed!")
