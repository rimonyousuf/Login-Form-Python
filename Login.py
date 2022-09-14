from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class login_windows:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1366x768+0+0')

        self.bg=ImageTk.PhotoImage(file=r'G:\Rimon Study\Login Form Project\img\bg.jpg')
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg='white')
        frame.place(x=500,y=140,width=340,height=450)

        img1=Image.open(r'G:\Rimon Study\Login Form Project\img\login.png')
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.loginimg=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.loginimg,bg='white')
        lblimg1.place(x=615,y=160,width=100,height=100)

if __name__=="__main__":
    root=Tk()
    app=login_windows(root)
    root.mainloop()