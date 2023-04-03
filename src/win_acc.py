import string, random, threading, time, os, sys, subprocess

def createaccsloop(accname):
    try:
        nums = string.digits
        new = ''.join(random.choice(nums) for i in range(5))
        print(Fore.GREEN + f"Adding new user: {accname}{new}")
        subprocess.os.system(f'net user {accname}{new} {accname}{new} /add')
        print(Fore.GREEN + f"Successfully added new user! User: {accname}{new}")
    except:
        print(Fore.RED + 'Failed!')
        pass