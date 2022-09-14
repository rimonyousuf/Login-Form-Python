from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class login_windows:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1366x768+0+0')

        #Background 
        self.bg=ImageTk.PhotoImage(file=r'G:\Rimon Study\Login Form Project\img\bg.jpg')
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg='white')
        frame.place(x=500,y=140,width=340,height=450)

        #Login 
        img1=Image.open(r'G:\Rimon Study\Login Form Project\img\login.png')
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.loginimg=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.loginimg,bg='white')
        lblimg1.place(x=615,y=150,width=100,height=100)

        get_str=Label(frame,text='Get Started',font=('times new roman',20,'bold'),fg='black',bg='white')
        get_str.place(x=95,y=110)


        #Username
        username=Label(frame,text='Username',font=('times new roman',15,'bold'),fg='black',bg='white')
        username.place(x=65,y=160)

        self.textuser=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.textuser.place(x=40,y=190,width=270)


        #Password
        password=Label(frame,text='Password',font=('times new roman',15,'bold'),fg='black',bg='white')
        password.place(x=65,y=220)

        self.textpass=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.textpass.place(x=40,y=250,width=270)


        #Username Icon
        img2=Image.open(r'G:\Rimon Study\Login Form Project\img\user.png')
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.loginimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.loginimg2,bg='white')
        lblimg2.place(x=40,y=160,width=25,height=25)


        #Password Icon
        img3=Image.open(r'G:\Rimon Study\Login Form Project\img\pass.jpg')
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.loginimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.loginimg3,bg='white')
        lblimg3.place(x=40,y=220,width=25,height=25)


        #Login Button
        login_btn=Button(frame,command=self.login,text='Login',font=('times new roman',15,'bold'),bd=1,relief=RIDGE,fg='white',bg='green',activeforeground='white',activebackground='green')
        login_btn.place(x=110,y=300,width=100,height=25)

        #Register Button
        reg_btn=Button(frame,text='New user registration',font=('times new roman',12,'bold'),borderwidth=0,fg='black',bg='white',activeforeground='black',activebackground='white')
        reg_btn.place(x=20,y=350,width=160)

        #Forget Password Button
        fgt_pass=Button(frame,text='Forget password',font=('times new roman',12,'bold'),borderwidth=0,fg='black',bg='white',activeforeground='black',activebackground='white')
        fgt_pass.place(x=20,y=380,width=130)


    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.textuser.get()=="Ri" and self.textpass.get()=="Mon":
            messagebox.showinfo("Success","You have successfully login")
        else:
            messagebox.showerror("Error","Invalid username or password")




if __name__=="__main__":
    root=Tk()
    app=login_windows(root)
    root.mainloop()