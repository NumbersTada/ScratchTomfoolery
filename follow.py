import scratchattach,random,json,time,ctypes
from threading import Thread
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),7)
print("\033[42m Scratch Follow Bot \033[40m\n\033[42m by NumbersTada     \033[40m")
def rs(length): return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=length))
def readAccounts(file):
    with open(file,"r") as f: a=f.read()
    return a.split("\n")
def bot(user,pw,u):
    try:
        print("\033[33m[LOGIN]\033[37m         "+user)
        session=scratchattach.login(user,"kocicka1")
        print("\033[35m[LOADING]\033[37m       "+user)
        us=session.connect_user(u)
        us.follow()
        print("\033[32m[SUCCESS]\033[37m       "+user)
    except Exception as e:
        print("\033[31m[ERROR]\033[37m         "+user+": "+str(e))
u=input("\033[36m[INPUT]\033[37m         Username: ")
accounts=readAccounts("accounts.txt")
with open("password.txt") as f: password=f.read()
for name in accounts:
    Thread(target=bot,args=(name,password,u)).start()
