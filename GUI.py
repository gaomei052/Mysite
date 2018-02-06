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


    G = gui('Center Manage')
    G.Button('Deploy',onLine,0,0,width=15)
    G.Button("Assets Messagement",ass,1,0,width=15)
    G.loop()

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

    G = gui('Login')
    G.Lable('User',0,0)
    user = G.Entry(0,1,columnspan=2)
    G.Lable('Password',1,0)
    password = G.Entry(1,1,show='*',columnspan=2,key='<Return>',fun=verifUserEvent)
    G.Button('Exit',quit,2,0)
    G.Button('Login',verifUser,2,1)
    G.loop()


if __name__ == '__main__':
    login()