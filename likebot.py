import scratchattach,random,json,ctypes
from threading import Thread
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),7)
print("\033[45m Scratch Love/Favorite Bot \033[40m\n\033[45m by NumbersTada            \033[40m")
def rs(length): return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=length))
def readAccounts(file):
    with open(file,"r") as f: a=f.read()
    return a.split("\n")
def bot(user,pw,pid):
    try:
        print("\033[33m[LOGIN]\033[37m         "+user)
        session=scratchattach.login(user,pw)
        print("\033[35m[LOADING]\033[37m       "+user)
        project=session.connect_project(pid)
        project.love()
        print("\033[32m[SUCCESS]\033[37m       "+user+": \033[31mlove\033[37m")
        project.favorite()
        print("\033[32m[SUCCESS]\033[37m       "+user+": \033[33mfavorite\033[37m")
        while True:
            project.post_view()
            print("\033[32m[SUCCESS]\033[37m       "+user+": \033[36mview\033[37m")
    except:
        print("\033[31m[ERROR]\033[37m         "+user+": "+str(e))
pid=int(input("\033[36m[INPUT]\033[37m         ID: "))
accounts=readAccounts("accounts.txt")
with open("password.txt") as f: password=f.read()
for name in accounts:
    Thread(target=bot,args=(name,password,pid)).start()
