import scratchattach,random,json,ctypes
from threading import Thread
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),7)
print("\033[44m Scratch Comment Bot \033[40m\n\033[44m by NumbersTada      \033[40m")
def rs(length): return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=length))
def readAccounts(file):
    with open(file,"r") as f: a=f.read()
    return a.split("\n")
def comment(user,pw,pid,text):
    try:
        print("\033[33m[LOGIN]\033[37m         "+user)
        session=scratchattach.login(user,pw)
        print("\033[35m[LOADING]\033[37m       "+user)
        project=session.connect_project(pid)
        comment=text
        while True:
            c=project.post_comment(content=comment)
            try:
                if c["status"] == {}:
                    print("\033[31m[ERROR]\033[37m         "+user)
            except:
                print("\033[32m[SUCCESS]\033[37m       "+user+" ("+str(c["id"])+")")
    except Exception as e:
        print("\033[31m[ERROR]\033[37m         "+user+": "+str(e))
pid=int(input("\033[36m[INPUT]\033[37m         ID: "))
c=input("\033[36m[INPUT]\033[37m         Comment: ")
accounts=readAccounts("accounts.txt")
with open("password.txt") as f: password=f.read()
for name in accounts:
    Thread(target=comment,args=(name,password,pid,c)).start()
