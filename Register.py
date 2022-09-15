from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry('1366x768+0+0')

        #Background
        self.bg=ImageTk.PhotoImage(file=r'G:\Rimon Study\Login Form Project\img\rbg.jpg')
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #Left Side Image
        self.bg1=ImageTk.PhotoImage(file=r'G:\Rimon Study\Login Form Project\img\rlf.jpg')
        lf_img=Label(self.root,image=self.bg1)
        lf_img.place(x=70,y=100,width=420,height=500)

        #Main Frame
        frame=Frame(self.root,bg='white')
        frame.place(x=490,y=100,width=770,height=500)

        reg_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,"bold"),fg='darkgreen',bg='white')
        reg_lbl.place(x=250,y=20)



if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()