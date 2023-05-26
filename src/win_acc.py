import random
import subprocess
import threading

config = {
    "Threads":10,
    "AccountNames":"Penis,IloveDick,Idk"
    
}

class AccountCreator:
    def __init__(self, accname):
        self.accname = accname

    def create_account(self):
        new = ''.join(random.choice(9999) for _ in range(5))
        try:
            print(f"Adding new user: {self.accname}{new}")
            subprocess.os.system(f'net user {self.accname}{new} {self.accname}{new} /add')
            print(f"Successfully added new user! User: {self.accname}{new}")
        except:
            print(f'Failed!')


def loop(accname):
    account_creator = AccountCreator(accname)
    account_creator.create_account()



def main():
    

    threads = []
    
    for v in range(config['Threads']):
        account_names = config['AccountNames'].split(',')
        t = threading.Thread(target=loop, args=(account_names,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        

if __name__ == '__main__':
    main()


# dont know if this works , because i dont want to test it lmao
