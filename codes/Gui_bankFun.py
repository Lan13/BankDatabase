import random

import pymysql
from tkinter import *

class BunkFunction(object):
    def __init__(self,dictUser):
        self.dictUser=dictUser
    def openUser(self):
        pass
    def setPasswd(self):
        pass



'''def welcomeView():
    global root
    root = Tk()
    root.title('科大破产银行登录界面')
    root.geometry('480x640')
    #账号块
    lb1=Label(root,text='管理员用户名：')
    lb1.place(relx=0.3,rely=0.3)
    global userE
    userE=Entry(root)
    userE.place(relx=0.5,rely=0.3)
    #密码块   其实我想在这里设置个DOWN或Return的快捷键然后setfocus到密码输入
    lb2=Label(root,text='密码：')
    lb2.place(relx=0.4,rely=0.4)
    global passwdE
    passwdE=Entry(root)
    passwdE.place(relx=0.5,rely=0.4)
    #登录块
    btn1=Button(root,text="登录",command=lambda:check(userE.get(),passwdE.get()))
    btn1.place(relx=0.3,rely=0.6)
    #退出块
    btn2=Button(root,text='退出',command=root.destroy)
    btn2.place(relx=0.6,rely=0.6)
    root.mainloop()
def check(user_entry,passwd_entry):
    user=str(user_entry)
    passwd=str(passwd_entry)
    if user not in dictUser:
        tkinter.messagebox.showinfo('科大破产银行','账号'+user+'不存在')
        userE.delete(0,END)
        passwdE.delete(0,END)
        return -1
    truepasswd=dictUser[user]
    if passwd != truepasswd:
        tkinter.messagebox.showwarning('科大破产银行','密码错误')
        userE.delete(0,END)
        passwdE.delete(0,END)
        return -1
    tkinter.messagebox.showinfo('科大破产银行','登录成功')
    userE.delete(0,END)
    passwdE.delete(0,END)
    login(root)
def login(root):
    global winNew
    winNew = Toplevel(root)
    winNew.geometry('480x640')
    winNew.title('科大破产银行')

    lbFun = Label(winNew,text='主功能')
    lbFun.place(relx=0.45,rely=0.3)

    btnOpen = Button(winNew,text='开户')  #command=...
    btnOpen.place(relx=0.4,rely=0.35)
    btnQuery = Button(winNew,text='查询')
    btnQuery.place(relx=0.5,rely=0.35)
    btnSave = Button(winNew,text='存款')
    btnSave.place(relx=0.4,rely=0.4)
    btnWithdraw = Button(winNew,text='取款')
    btnWithdraw.place(relx=0.5,rely=0.4)
    btnTransfer = Button(winNew,text='转账')
    btnTransfer.place(relx=0.4,rely=0.45)
    btnUpdate = Button(winNew,text='改密')
    btnUpdate.place(relx=0.5,rely=0.45)
    btnLock = Button(winNew,text='锁卡')
    btnLock.place(relx=0.4,rely=0.5)
    btnUnlock = Button(winNew,text='解锁')
    btnUnlock.place(relx=0.5,rely=0.5)
    btnReissue = Button(winNew,text='补卡')
    btnReissue.place(relx=0.4,rely=0.55)
    btnClose = Button(winNew,text='销户')
    btnClose.place(relx=0.5,rely=0.55)

    btnQuit = Button(winNew,text='退出',command=winNew.destroy)
    btnQuit.place(relx=0.45,rely=0.6)'''