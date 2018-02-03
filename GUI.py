#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# @Time     : 2018/2/2 下午2:24
# @Auther   : GaoMei
# @FileName : GUI.py
# @Software : PyCharm
# @Email    : gaomei052@gmail.com

from tkinter import *
from tkinter import ttk
from tkFileDialog import *
import tkMessageBox
from login import Login
from deployGui import Deploy
from modules.GuiApi import gui
import assetsManagement
import warnings

warnings.filterwarnings('ignore')


def main(user,password):
    def onLine():
        if Login(user,password).permissionValue() <= 1:
            Deploy()
        else:
            tkMessageBox.showinfo(title='Permission Error',message="You don't have access.")

    def ass():
        if Login(user,password).permissionValue() < 1:
            assetsManagement.asset()
        else:
            tkMessageBox.showinfo(title='Permission Error',message="You don't have access.")


    G = gui()
    G.Button('Deploy',onLine,0,0,width=15)
    G.Button("Assets Messagement",ass,1,0,width=15)

    #tk = Tk()
    #tk.title("Contorl Center")
    #Button(tk,text="Deploy",command=onLine).grid(row=0,column=0,columnspan=2)
    #Button(tk,text="Assets Management",command=ass).grid(row=1,column=0,columnspan=2)
    #tk.mainloop()

def login():
    def verifUser():
        l = Login(user.get(),password.get())
        reselt = l.verificationUser()
        if reselt == 1:

            main(user.get(),password.get())
        else:
            tkMessageBox.showinfo(title="Error", message="User or password is wrong")

    def verifUserEvent(event):
        verifUser()
    top = Tk()
    top.title("Login")
    Label(top,text='User').grid(row=0,column=0)
    user = StringVar()
    Entry(top,textvariable=user).grid(row=0,column=1,columnspan=2)
    Label(top,text='Password').grid(row=1,column=0)
    password = StringVar()
    passwd = Entry(top,textvariable=password)
    passwd.grid(row=1,column=1,columnspan=2)
    passwd['show'] = "*"
    passwd.bind('<Return>',verifUserEvent)
    Button(top,text='Exit',command=quit).grid(row=2,column=0)
    Button(top,text='Login',command=verifUser).grid(row=2,column=2)
    top.mainloop()




if __name__ == '__main__':
    login()