
from tkinter.simpledialog import *
import tkinter.messagebox
import random
import pymysql

# 管理员账号与密码
dictUser={'ljw':'123','':''}
# 数据库的连接

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='你的密码',
    db='test',
    charset='utf8mb4'
)
global curosr
cursor = db.cursor()

class Gui_Admin(object):
    def __init__(self,dictUser):
        self.dictUser = dictUser

    def welcomeView(self):
        self.root = Tk()
        self.root.title('欢迎来到科大破产银行')
        self.root.geometry('480x640')
        # 账号块
        lb1 = Label(self.root, text='管理员用户名：')
        lb1.place(relx=0.3, rely=0.3)
        global userE
        userE = Entry(self.root)
        userE.place(relx=0.5, rely=0.3)
        # 密码块   其实我想在这里设置个DOWN或Return的快捷键然后setfocus到密码输入
        lb2 = Label(self.root, text='密码：')
        lb2.place(relx=0.4, rely=0.4)
        global passwdE
        passwdE = Entry(self.root,show = '*' )
        passwdE.place(relx=0.5, rely=0.4)
        # 登录块
        btn1 = Button(self.root, text="登录", command=lambda: self.check(userE.get(), passwdE.get()))
        btn1.place(relx=0.3, rely=0.6)
        # 退出块
        btn2 = Button(self.root, text='退出', command=self.root.destroy)
        btn2.place(relx=0.6, rely=0.6)
        self.root.mainloop()

    def check(self,user_entry, passwd_entry):
        user = str(user_entry)
        passwd = str(passwd_entry)
        if user not in dictUser:
            tkinter.messagebox.showinfo('科大破产银行', '账号' + user + '不存在')
            userE.delete(0, END)
            passwdE.delete(0, END)
            userE.focus()
            return -1
        truepasswd = dictUser[user]
        if passwd != truepasswd:
            tkinter.messagebox.showwarning('科大破产银行', '密码错误')
            passwdE.delete(0, END)
            passwdE.focus()
            return -1
        tkinter.messagebox.showinfo('科大破产银行', '登录成功')
        userE.delete(0, END)
        passwdE.delete(0, END)
        self.login(self.root)

    def login(self,root):
        self.winFun = Toplevel(root)
        self.winFun.geometry('480x640')
        self.winFun.title('科大破产银行')
        #self.root.attributes("-disabled", 1)

        lbFun = Label(self.winFun, text='主功能')
        lbFun.place(relx=0.45, rely=0.3)

        btnOpen = Button(self.winFun, text='开户', command=self.openUser)  # command=...
        btnOpen.place(relx=0.4, rely=0.35)
        btnQuery = Button(self.winFun, text='查询',command=self.QueryUser)
        btnQuery.place(relx=0.5, rely=0.35)
        btnSave = Button(self.winFun, text='存款',command=self.saveUser)
        btnSave.place(relx=0.4, rely=0.4)
        btnWithdraw = Button(self.winFun, text='取款',command=self.withdrawUser)
        btnWithdraw.place(relx=0.5, rely=0.4)
        btnTransfer = Button(self.winFun, text='转账',command=self.transferUser)
        btnTransfer.place(relx=0.4, rely=0.45)
        btnUpdate = Button(self.winFun, text='改密',command=self.updateUser)
        btnUpdate.place(relx=0.5, rely=0.45)
        btnLock = Button(self.winFun, text='锁卡',command=self.lockUser)
        btnLock.place(relx=0.4, rely=0.5)
        btnUnlock = Button(self.winFun, text='解锁',command=self.unlockUser)
        btnUnlock.place(relx=0.5, rely=0.5)
        btnReissue = Button(self.winFun, text='补卡',command=self.reissueUser)
        btnReissue.place(relx=0.4, rely=0.55)
        btnClose = Button(self.winFun, text='销户',command=self.closeUser)
        btnClose.place(relx=0.5, rely=0.55)

        #self.winFun.protocol("WM_DELETE_WINDOW",self.winfunClose)
        btnQuit = Button(self.winFun, text='返回',
                         command=self.winFun.destroy)
        btnQuit.place(relx=0.45, rely=0.6)
    '''def winfunClose(self):
        self.winFun.destroy()
        self.root.attributes("-disabled",0)'''
    def openUser(self):
        self.openroot = Toplevel(self.winFun)
        self.openroot.title('科大破产银行开户界面')
        self.openroot.geometry('320x320')
        nameO = Entry(self.openroot)
        nameO.place(relx=0.5,rely=0.2)
        idCardO = Entry(self.openroot)
        idCardO.place(relx=0.5,rely=0.3)
        phoneO=Entry(self.openroot)
        phoneO.place(relx=0.5,rely=0.4)
        global passwdO1,passwdO2
        passwdO1 = Entry(self.openroot,show='*')
        passwdO1.place(relx=0.5,rely=0.5)
        passwdO2 = Entry(self.openroot,show='*')
        passwdO2.place(relx=0.5,rely=0.6)
        namelb=Label(self.openroot,text='请输入您的姓名：')
        namelb.place(relx=0,rely=0.2)
        idnumlb=Label(self.openroot,text='请输入您的身份证号码：')
        idnumlb.place(relx=0,rely=0.3)
        phonelb=Label(self.openroot,text='请输入您的电话号码：')
        phonelb.place(relx=0,rely=0.4)
        pwdlb1=Label(self.openroot,text='请输入您的密码：')
        pwdlb1.place(relx=0,rely=0.5)
        pwdlb2=Label(self.openroot,text='请再次输入您的密码：')
        pwdlb2.place(relx=0,rely=0.6)
        okbtn=Button(self.openroot,text='确认',command=
        lambda:self.createCardNumber(passwdO1.get(),passwdO2.get(),
                                     nameO.get(),idCardO.get(),
                                     phoneO.get()))
        okbtn.place(relx=0.3,rely=0.8)
        canclebtn=Button(self.openroot,text='返回',
                         command=lambda :[self.openroot.destroy(),self.winFun.focus()])
        canclebtn.place(relx=0.7,rely=0.8)
    def createCardNumber(self,pwd1,pwd2,nameO,idCardO,phoneO):
        strpwd1=str(pwd1)
        strpwd2=str(pwd2)
        name = str(nameO)
        idCard = str(idCardO)
        phone = str(phoneO)
        if strpwd1 != strpwd2:
            tkinter.messagebox.showwarning('科大破产银行','两次密码不同，请重新输入')
            passwdO1.delete(0,END)
            passwdO2.delete(0,END)
            passwdO1.focus()
        if strpwd1 == strpwd2 and strpwd1 != "" and name != "" and idCard !="" and phone != "" :
            passwd=strpwd1
            while True:
                cardNumber =""
                for i in range(6):
                    cardNumber += str(random.randrange(0,10))
                cursor.execute("SELECT * FROM card where cardNumber = '%s'" % cardNumber)
                card = cursor.fetchone()
                if card is None:
                    break

            sql = "INSERT INTO user VALUES(%s,%s,%s,%s)"
            cursor.execute(sql,(name,idCard,phone,cardNumber))
            db.commit()
            sql = "INSERT INTO card VALUES(%s,%s,%s,%s)"
            cursor.execute(sql,(cardNumber,passwd,0.0,1))
            db.commit()
            tkinter.messagebox.showinfo('科大破产银行',"%s,你好,你的卡号是%s" % (name,cardNumber))
            self.openroot.destroy()
            self.winFun.focus()
    def QueryUser(self):
        self.queryroot = Toplevel(self.winFun)
        self.queryroot.title('科大破产银行查询界面')
        self.queryroot.geometry('320x320')
        global cardNumQ, passwdQ
        cardNumQ = Entry(self.queryroot)
        cardNumQ.place(relx=0.5,rely=0.3)
        lbcard = Label(self.queryroot,text='请输入您的卡号：')
        lbcard.place(relx=0.1,rely=0.3)
        passwdQ = Entry(self.queryroot,show='*')
        passwdQ.place(relx=0.5,rely=0.4)
        lbpasswd = Label(self.queryroot,text='请输入您的密码：')
        lbpasswd.place(relx=0.1,rely=0.4)
        btnok = Button(self.queryroot,text="查询",
                       command = lambda:self.queryFun(cardNumQ.get(),passwdQ.get()) )

        btnok.place(relx=0.3,rely=0.8)
        btncancel = Button(self.queryroot,text="返回",
                           command=lambda :[self.queryroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7,rely=0.8)

    def queryFun(self,cardNumfun,passwdfun):
        cardnumber = str(cardNumfun)
        passwd = str(passwdfun)
        cursor.execute("SELECT * FROM card where cardNumber = '%s'" % cardnumber)
        card = cursor.fetchone()

        if card is None:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
            cardNumQ.delete(0, END)
            passwdQ.delete(0, END)
            cardNumQ.focus()
        elif card[3] == 0:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您的卡已经被锁定")
            cardNumQ.delete(0, END)
            passwdQ.delete(0, END)
            cardNumQ.focus()
        elif passwd == card[1]:
            cursor.execute("SELECT * FROM user where cardNumber = '%s'" % cardnumber)
            data = cursor.fetchall()[0]
            tkinter.messagebox.showinfo("科大破产银行", "'%s',您好,您的余额为：'%s'" % (data[0],card[2]))
            self.queryroot.destroy()
            self.winFun.focus()
        else:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
            passwdQ.delete(0,END)
            passwdQ.focus()
    def saveUser(self):
        self.saveroot = Toplevel(self.winFun)
        self.saveroot.title('科大破产银行存款界面')
        self.saveroot.geometry('320x320')

        global cardNumS, passwdS, moneyS
        cardNumS = Entry(self.saveroot)
        cardNumS.place(relx=0.5,rely=0.3)
        passwdS = Entry(self.saveroot,show='*')
        passwdS.place(relx=0.5,rely=0.4)
        moneyS = Entry(self.saveroot)
        moneyS.place(relx=0.5,rely=0.5)
        lbcard = Label(self.saveroot, text='请输入您的卡号：')
        lbcard.place(relx=0.1, rely=0.3)
        lbpasswd = Label(self.saveroot, text='请输入您的密码：')
        lbpasswd.place(relx=0.1, rely=0.4)
        lbmoney = Label(self.saveroot,text="存款金额:")
        lbmoney.place(relx=0.1,rely=0.5)
        btnok = Button(self.saveroot, text="确定",
                       command=lambda: self.saveFun(cardNumS.get(),
                                                    passwdS.get(),
                                                    moneyS.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.saveroot, text="返回",
                           command=lambda :[self.saveroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def saveFun(self,cardNumfun,passwdfun,moneyfun):
        cardnumber=str(cardNumfun)
        passwd=str(passwdfun)
        moneysave=float(moneyfun)
        cursor.execute("SELECT * FROM card where cardNumber = '%s'" % cardnumber)
        card = cursor.fetchone()

        if card is None:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
            cardNumS.delete(0, END)
            passwdS.delete(0, END)
            moneyS.delete(0,END)
            cardNumS.focus()
        elif card[3] == 0:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您的卡已经被锁定")
            cardNumS.delete(0, END)
            passwdS.delete(0, END)
            moneyS.delete(0,END)
            cardNumS.focus()
        elif passwd == card[1]:
            cursor.execute("SELECT * FROM user where cardNumber = '%s'" % cardnumber)
            data = cursor.fetchall()[0]
            nowmoney =str(float(card[2])+moneysave)
            cursor.execute("UPDATE card SET money = '%s' where cardNumber = '%s'" %(nowmoney,cardnumber))
            db.commit()
            tkinter.messagebox.showinfo('科大破产银行'," %s您好，存款成功，当前可用余额为：%s元"%(data[0],nowmoney))

            self.saveroot.destroy()
            self.winFun.focus()
        else:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
            passwdS.delete(0,END)
            moneyS.delete(0,END)
            passwdS.focus()
    def withdrawUser(self):
        self.withdrawroot = Toplevel(self.winFun)
        self.withdrawroot.title('科大破产银行取款界面')
        self.withdrawroot.geometry('320x320')
        global cardNumW, passwdW, moneyW
        cardNumW = Entry(self.withdrawroot)
        cardNumW.place(relx=0.5, rely=0.3)
        passwdW = Entry(self.withdrawroot,show='*')
        passwdW.place(relx=0.5, rely=0.4)
        moneyW = Entry(self.withdrawroot)
        moneyW.place(relx=0.5, rely=0.5)
        lbcard = Label(self.withdrawroot, text='请输入您的卡号：')
        lbcard.place(relx=0.1, rely=0.3)
        lbpasswd = Label(self.withdrawroot, text='请输入您的密码：')
        lbpasswd.place(relx=0.1, rely=0.4)
        lbmoney = Label(self.withdrawroot, text="取款金额:")
        lbmoney.place(relx=0.1, rely=0.5)
        btnok = Button(self.withdrawroot, text="确定",
                       command=lambda: self.withdrawFun(cardNumW.get(),
                                                    passwdW.get(),
                                                    moneyW.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.withdrawroot, text="返回",
                           command=lambda:[self.withdrawroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def withdrawFun(self,cardNumfun,passwdfun,moneyfun):
        cardnumber=str(cardNumfun)
        passwd=str(passwdfun)
        moneywithdraw=float(moneyfun)
        cursor.execute("SELECT * FROM card where cardNumber = '%s'" % cardnumber)
        card = cursor.fetchone()

        if card is None:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
            cardNumW.delete(0, END)
            passwdW.delete(0, END)
            moneyW.delete(0,END)
            cardNumW.focus()
        elif card[3] == 0:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您的卡已经被锁定")
            cardNumW.delete(0, END)
            passwdW.delete(0, END)
            moneyW.delete(0,END)
            cardNumW.focus()
        elif passwd == card[1]:
            cursor.execute("SELECT * FROM user where cardNumber = '%s'" % cardnumber)
            data = cursor.fetchall()[0]
            if moneywithdraw <= float(card[2]):
                nowmoney =str(float(card[2])-moneywithdraw)
                cursor.execute("UPDATE card SET money = '%s' where cardNumber = '%s'" %(nowmoney,cardnumber))
                db.commit()
                tkinter.messagebox.showinfo('科大破产银行'," %s您好，取款成功,取款金额为：%s元,当前可用余额为：%s元"%(data[0],moneywithdraw,nowmoney))
                self.withdrawroot.destroy()
                self.winFun.focus()
            else:
                tkinter.messagebox.showwarning('科大破产银行',"对不起，余额不足，您当前的余额为:%s元" %float(card[2]))
                moneyW.delete(0,END)
                moneyW.focus()
        else:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
            passwdW.delete(0,END)
            moneyW.delete(0,END)
            passwdW.focus()
    def transferUser(self):
        self.transferroot=Toplevel(self.winFun)
        self.transferroot.title('科大破产银行转账界面')
        self.transferroot.geometry('320x320')

        global cardNumTr, passwdTr, receuserTr, moneyTr
        cardNumTr = Entry(self.transferroot)
        cardNumTr.place(relx=0.5, rely=0.3)
        passwdTr = Entry(self.transferroot,show='*')
        passwdTr.place(relx=0.5, rely=0.4)
        receuserTr = Entry(self.transferroot)
        receuserTr.place(relx=0.5, rely=0.5)
        moneyTr = Entry(self.transferroot)
        moneyTr.place(relx=0.5, rely=0.6)
        lbcard = Label(self.transferroot, text='请输入您的卡号：')
        lbcard.place(relx=0.1, rely=0.3)
        lbpasswd = Label(self.transferroot, text='请输入您的密码：')
        lbpasswd.place(relx=0.1, rely=0.4)
        lbuser = Label(self.transferroot,text='转入账号：')
        lbuser.place(relx=0.1,rely=0.5)
        lbmoney = Label(self.transferroot, text="转账金额:")
        lbmoney.place(relx=0.1, rely=0.6)
        btnok = Button(self.transferroot, text="确定",
                       command=lambda: self.transferFun(cardNumTr.get(),
                                                        passwdTr.get(),
                                                        receuserTr.get(),
                                                        moneyTr.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.transferroot, text="返回",
                           command=lambda :[self.transferroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def transferFun(self,cardNumfun,passwdfun,receuserfun,moneyfun):
        cardnumber=str(cardNumfun)
        passwd=str(passwdfun)
        receuser=str(receuserfun)
        moneytransfer=float(moneyfun)
        if cardnumber != "" and passwd != "" and receuser != "":
            cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'" % cardnumber)
            card = cursor.fetchone()
            cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'" % receuser)
            rececard = cursor.fetchone()
            if card is None:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
                cardNumTr.delete(0, END)
                passwdTr.delete(0, END)
                receuserTr.delete(0, END)
                moneyTr.delete(0, END)
                cardNumTr.focus()
            elif card[3] == 0:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您的卡已经被锁定")
                cardNumTr.delete(0, END)
                passwdTr.delete(0, END)
                receuserTr.delete(0, END)
                moneyTr.delete(0, END)
                cardNumTr.focus()
            elif rececard is None:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，对方的卡号不存在！")
                receuserTr.delete(0, END)
                receuserTr.focus()
            elif rececard[3] == 0:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，对方的卡已经被锁定")
                receuserTr.delete(0, END)
                moneyTr.delete(0, END)
                cardNumTr.focus()
            elif passwd == card[1]:
                cursor.execute("SELECT * FROM user where cardNumber = '%s'" % cardnumber)
                data = cursor.fetchall()[0]
                if moneytransfer <= float(card[2]):
                    nowmoney = str(float(card[2]) - moneytransfer)
                    cursor.execute("UPDATE card SET money = '%s' WHERE cardNumber = '%s'" % (nowmoney, cardnumber))
                    db.commit()
                    usermoney = str(float(rececard[2]) + moneytransfer)
                    cursor.execute("UPDATE card SET money = '%s' WHERE cardNumber = '%s'" % (usermoney, receuser))
                    db.commit()
                    tkinter.messagebox.showinfo('科大破产银行', " %s您好，转账成功,转账金额为：%s元,当前可用余额为：%s元"
                                                % (data[0], moneytransfer, nowmoney))
                    self.transferroot.destroy()
                    self.winFun.focus()
                else:
                    tkinter.messagebox.showwarning('科大破产银行', "对不起，余额不足，您当前的余额为:%s元" % float(card[2]))
                    moneyTr.delete(0, END)
                    moneyTr.focus()
            else:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
                passwdTr.delete(0, END)
                receuserTr.delete(0, END)
                moneyTr.delete(0, END)
                passwdTr.focus()
    def updateUser(self):
        self.updateroot = Toplevel(self.winFun)
        self.updateroot.title('科大破产银行改密界面')
        self.updateroot.geometry('320x320')

        global cardNumU, passwdU, newpwdU1, newpwdU2
        cardNumU = Entry(self.updateroot)
        cardNumU.place(relx=0.5, rely=0.3)
        passwdU = Entry(self.updateroot,show='*')
        passwdU.place(relx=0.5, rely=0.4)
        newpwdU1 = Entry(self.updateroot,show='*')
        newpwdU1.place(relx=0.5, rely=0.5)
        newpwdU2 = Entry(self.updateroot,show='*')
        newpwdU2.place(relx=0.5, rely=0.6)
        lbcard = Label(self.updateroot, text='请输入您的卡号：')
        lbcard.place(relx=0.1, rely=0.3)
        lbpasswd = Label(self.updateroot, text='请输入您的密码：')
        lbpasswd.place(relx=0.1, rely=0.4)
        lbpwd1 = Label(self.updateroot, text='请输入新的密码：')
        lbpwd1.place(relx=0.1, rely=0.5)
        lbpwd2 = Label(self.updateroot, text="请再次输入新的密码:")
        lbpwd2.place(relx=0.1, rely=0.6)
        btnok = Button(self.updateroot, text="确定",
                       command=lambda: self.updateFun(cardNumU.get(),
                                                      passwdU.get(),
                                                      newpwdU1.get(),
                                                      newpwdU2.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.updateroot, text="返回",
                           command=lambda :[self.updateroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def updateFun(self,cardnumfun,passwdfun,pwdfun1,pwdfun2):
        cardnumber = str(cardnumfun)
        passwd = str(passwdfun)
        pwd1 = str(pwdfun1)
        pwd2 = str(pwdfun2)
        if cardnumber != "" and passwd != "" and pwd1 != "" and pwd2 !="":
            cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'" % cardnumber)
            card = cursor.fetchone()

            if card is None:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
                cardNumU.delete(0, END)
                passwdU.delete(0, END)
                newpwdU1.delete(0, END)
                newpwdU2.delete(0, END)
                cardNumU.focus()
            elif passwd == card[1]:
                if pwd1 == pwd2:
                   cursor.execute("UPDATE card SET passwd = '%s' WHERE cardNumber = '%s'"
                                  %(pwd1,cardnumber))
                   db.commit()
                   tkinter.messagebox.showinfo('科大破产银行','修改密码成功！')
                   self.updateroot.destroy()
                   self.winFun.focus()
                else:
                    tkinter.messagebox.showwarning('科大破产银行','对不起，您两次输入的密码不相同')
                    newpwdU1.delete(0,END)
                    newpwdU2.delete(0,END)
                    newpwdU1.focus()
            else:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
                passwdU.delete(0, END)
                newpwdU1.delete(0, END)
                newpwdU2.delete(0, END)
                passwdU.focus()
    def lockUser(self):
        self.lockroot = Toplevel(self.winFun)
        self.lockroot.title('科大破产银行锁卡界面')
        self.lockroot.geometry('320x320')

        global cardNumL, passwdL
        cardNumL = Entry(self.lockroot)
        cardNumL.place(relx=0.5,rely=0.4)
        passwdL = Entry(self.lockroot,show='*')
        passwdL.place(relx=0.5,rely=0.5)
        lbcard = Label(self.lockroot, text='请输入您的卡号：')
        lbcard.place(relx=0.1, rely=0.4)
        lbpasswd = Label(self.lockroot, text='请输入您的密码：')
        lbpasswd.place(relx=0.1, rely=0.5)
        btnok = Button(self.lockroot, text="确定",
                       command=lambda: self.lockFun(cardNumL.get(),passwdL.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.lockroot, text="返回",
                           command=lambda :[self.lockroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def lockFun(self,cardnumfun,passwdfun):
        askback = tkinter.messagebox.askyesno('科大破产银行','确定要锁定这张卡？')
        if askback == True:
            cardnumber = str(cardnumfun)
            passwd = str(passwdfun)
            cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'" %cardnumber)
            card = cursor.fetchone()

            if card is None:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
                cardNumL.delete(0, END)
                passwdL.delete(0, END)
                cardNumL.focus()
            elif passwd == card[1]:
                cursor.execute("UPDATE card SET isLock = 0 WHERE cardNumber = '%s'"
                               %cardnumber)
                db.commit()
                tkinter.messagebox.showinfo('科大破产银行','您的账户已经成功锁定')
                self.lockroot.destroy()
                self.winFun.focus()
            else:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
                passwdL.delete(0, END)
                passwdL.focus()
        else:
            cardNumL.delete(0, END)
            passwdL.delete(0, END)
            cardNumL.focus()
    def unlockUser(self):
        self.unlockroot = Toplevel(self.winFun)
        self.unlockroot.title('科大破产银行解锁界面')
        self.unlockroot.geometry('320x320')

        global cardNumUl, passwdUl
        cardNumUl = Entry(self.unlockroot)
        cardNumUl.place(relx=0.5, rely=0.4)
        passwdUl = Entry(self.unlockroot,show='*')
        passwdUl.place(relx=0.5, rely=0.5)
        lbcard = Label(self.unlockroot, text='请输入您的卡号：')
        lbcard.place(relx=0.1, rely=0.4)
        lbpasswd = Label(self.unlockroot, text='请输入您的密码：')
        lbpasswd.place(relx=0.1, rely=0.5)
        btnok = Button(self.unlockroot, text="确定",
                       command=lambda: self.unlockFun(cardNumUl.get(), passwdUl.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.unlockroot, text="返回",
                           command=lambda :[self.unlockroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def unlockFun(self,cardnumfun,passwdfun):
        cardnumber = str(cardnumfun)
        passwd = str(passwdfun)
        cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'"%cardnumber)
        card=cursor.fetchone()

        if card is None:
            tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的卡号不存在！")
            cardNumUl.delete(0, END)
            passwdUl.delete(0, END)
            cardNumUl.focus()
        elif passwd == card[1]:
            cursor.execute("UPDATE card SET isLock = 1 WHERE cardNumber = '%s'"
                            %cardnumber)
            db.commit()
            tkinter.messagebox.showinfo('科大破产银行','您的账户已经成功解锁')
            self.unlockroot.destroy()
            self.winFun.focus()
        else:
            tkinter.messagebox.showwarning('科大破产银行','对不起，您输入的密码错误')
            passwdUl.delete(0, END)
            passwdUl.focus()
    def reissueUser(self):
        self.reissueroot=Toplevel(self.winFun)
        self.reissueroot.title('科大破产银行补卡界面')
        self.reissueroot.geometry('320x320')

        global nameR, idcardR, cardNumR, passwdR
        nameR = Entry(self.reissueroot)
        nameR.place(relx=0.5, rely=0.3)
        idcardR = Entry(self.reissueroot)
        idcardR.place(relx=0.5, rely=0.4)
        cardNumR = Entry(self.reissueroot)
        cardNumR.place(relx=0.5, rely=0.5)
        passwdR = Entry(self.reissueroot,show='*')
        passwdR.place(relx=0.5, rely=0.6)
        lbname = Label(self.reissueroot, text='请输入您的姓名：')
        lbname.place(relx=0, rely=0.3)
        lbidcard = Label(self.reissueroot,text='请输入您的身份证号码：')
        lbidcard.place(relx=0, rely=0.4)
        lbcardnum = Label(self.reissueroot, text='请输入您丢失的卡号：')
        lbcardnum.place(relx=0, rely=0.5)
        lbpasswd = Label(self.reissueroot, text="请输入您的密码:")
        lbpasswd.place(relx=0,rely=0.6)
        btnok = Button(self.reissueroot, text="补卡",
                       command=lambda: self.reissueFun(nameR.get(),
                                                       idcardR.get(),
                                                       cardNumR.get(),
                                                       passwdR.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.reissueroot, text="返回",
                           command=lambda :[self.reissueroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)
    def reissueFun(self,namefun,idcardfun,cardnumfun,passwdfun):
        name = str(namefun)
        idcard = str(idcardfun)
        cardnumber=str(cardnumfun)
        passwd = str(passwdfun)

        if name != "" and idcard != "" and cardnumber !="" and passwd !="":
            cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'" % cardnumber)
            card = cursor.fetchone()
            cursor.execute("SELECT * FROM user WHERE cardNumber = '%s'" % cardnumber)
            user = cursor.fetchone()

            if card is None or name not in user or idcard not in user:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的信息有误")
                nameR.delete(0, END)
                idcardR.delete(0, END)
                cardNumR.delete(0, END)
                passwdR.delete(0, END)
                nameR.focus()
            elif passwd == card[1]:
                while True:
                    newcardnumber = ""
                    for i in range(6):
                        newcardnumber += str(random.randrange(0, 10))
                    cursor.execute("SELECT * FROM card where cardNumber = '%s'" % newcardnumber)
                    card = cursor.fetchone()
                    if card is None:
                        break
                cursor.execute("UPDATE card SET cardNumber = '%s' WHERE cardNumber = '%s'"
                               %(newcardnumber,cardnumber))
                db.commit()
                cursor.execute("UPDATE user SET cardNumber = '%s' WHERE cardNumber = '%s'"
                               %(newcardnumber,cardnumber))
                db.commit()
                tkinter.messagebox.showinfo('科大破产银行',"补卡成功，您的新卡号为： %s"
                                            %newcardnumber)
                self.reissueroot.destroy()
                self.winFun.focus()
            else:
                tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
                passwdR.delete(0,END)
                passwdR.focus()
    def closeUser(self):
        self.closeroot = Toplevel(self.winFun)
        self.closeroot.title('科大破产银行销户界面')
        self.closeroot.geometry('320x320')

        global nameC, idcardC, cardNumC, passwdC
        nameC = Entry(self.closeroot)
        nameC.place(relx=0.5, rely=0.3)
        idcardC = Entry(self.closeroot)
        idcardC.place(relx=0.5, rely=0.4)
        cardNumC = Entry(self.closeroot)
        cardNumC.place(relx=0.5, rely=0.5)
        passwdC = Entry(self.closeroot,show='*')
        passwdC.place(relx=0.5, rely=0.6)
        lbname = Label(self.closeroot, text='请输入您的姓名：')
        lbname.place(relx=0, rely=0.3)
        lbidcard = Label(self.closeroot, text='请输入您的身份证号码：')
        lbidcard.place(relx=0, rely=0.4)
        lbcardnum = Label(self.closeroot, text='请输入您要注销的卡号：')
        lbcardnum.place(relx=0, rely=0.5)
        lbpasswd = Label(self.closeroot, text="请输入您的密码:")
        lbpasswd.place(relx=0, rely=0.6)
        btnok = Button(self.closeroot, text="注销",
                       command=lambda: self.closeFun(nameC.get(),
                                                       idcardC.get(),
                                                       cardNumC.get(),
                                                       passwdC.get()))
        btnok.place(relx=0.3, rely=0.8)
        btncancel = Button(self.closeroot, text="返回",
                           command=lambda :[self.closeroot.destroy(),self.winFun.focus()])
        btncancel.place(relx=0.7, rely=0.8)

    def closeFun(self, namefun, idcardfun, cardnumfun, passwdfun):
        name = str(namefun)
        idcard = str(idcardfun)
        cardnumber = str(cardnumfun)
        passwd = str(passwdfun)
        askback = tkinter.messagebox.askyesno('科大破产银行','确定要注销该卡吗？')
        if askback == True:
            if name != "" and idcard != "" and cardnumber != "" and passwd != "":
                cursor.execute("SELECT * FROM card WHERE cardNumber = '%s'" % cardnumber)
                card = cursor.fetchone()
                cursor.execute("SELECT * FROM user WHERE cardNumber = '%s'" % cardnumber)
                user = cursor.fetchone()

                if card is None or name not in user or idcard not in user:
                    tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的信息有误")
                    nameC.delete(0, END)
                    idcardC.delete(0, END)
                    cardNumC.delete(0, END)
                    passwdC.delete(0, END)
                    nameC.focus()
                elif passwd == card[1]:
                    cursor.execute("DELETE FROM test.card WHERE cardNumber = '%s'"
                                   % cardnumber)
                    db.commit()
                    cursor.execute("DELETE FROM test.user WHERE cardNumber = '%s'"
                                   % cardnumber)
                    db.commit()
                    tkinter.messagebox.showinfo('科大破产银行',
                                                '注销成功，%s已经被注销'% cardnumber)
                    self.closeroot.destroy()
                    self.winFun.focus()
                else:
                    tkinter.messagebox.showwarning("科大破产银行", "对不起，您输入的密码错误")
                    passwdC.delete(0, END)
                    passwdC.focus()
            else:
                nameC.delete(0, END)
                idcardC.delete(0, END)
                cardNumC.delete(0, END)
                passwdC.delete(0, END)
                nameC.focus()

