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

        #Register
        reg_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,"bold"),fg='darkgreen',bg='white')
        reg_lbl.place(x=260,y=20)

        #First Name
        fname=Label(frame,text='First Name',font=('times new roman',15,'bold'),bg='white')
        fname.place(x=20,y=100)

        fname_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        fname_ent.place(x=20,y=130,width=250)

        #Last Name
        lname=Label(frame,text='Last Name',font=('times new roman',15,'bold'),bg='white')
        lname.place(x=340,y=100)

        lname_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        lname_ent.place(x=340,y=130,width=250)

        #Contact
        contact=Label(frame,text='Contact No',font=('times new roman',15,'bold'),bg='white')
        contact.place(x=20,y=170)

        contact_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        contact_ent.place(x=20,y=200,width=250)

        #Email
        email=Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white')
        email.place(x=340,y=170)

        email_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        email_ent.place(x=340,y=200,width=250)

        #Security Question
        security_q=Label(frame,text='Security Question',font=('times new roman',15,'bold'),bg='white')
        security_q.place(x=20,y=240)

        security_cmbo=ttk.Combobox(frame,font=('times new roman',12,'bold'),state='readonly')
        security_cmbo['values']=('Select','What is your birth place?','Who is your girlfriend?','What is your pet name?')
        security_cmbo.place(x=20,y=270,width=250)
        security_cmbo.current(0)

        security_ans=Label(frame,text='Answer',font=('times new roman',15,'bold'),bg='white')
        security_ans.place(x=340,y=240)

        security_ans_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        security_ans_ent.place(x=340,y=270,width=250)

        #Password
        passw=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white')
        passw.place(x=20,y=310)

        passw_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        passw_ent.place(x=20,y=340,width=250)

        passw_cnf=Label(frame,text='Confirm Password',font=('times new roman',15,'bold'),bg='white')
        passw_cnf.place(x=340,y=310)

        passw_cnf_ent=ttk.Entry(frame,font=('times new roman',15,'bold'))
        passw_cnf_ent.place(x=340,y=340,width=250)

        #Checkbox
        checkbtn=Checkbutton(frame,text='I agree the terms & conditions',font=('times new roman',12,'bold'),bg='white',activebackground='white',onvalue=1,offvalue=0)
        checkbtn.place(x=20,y=380)

        #Regester Button
        img=Image.open(r'G:\Rimon Study\Login Form Project\img\reg.png')
        img=img.resize((120,40),Image.ANTIALIAS)
        self.pict=ImageTk.PhotoImage(img)
        reg_btn=Button(frame,image=self.pict,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'),bg='white')
        reg_btn.place(x=20,y=420,width=180)

        #Login Button
        img2=Image.open(r'G:\Rimon Study\Login Form Project\img\lg.jpg')
        img2=img2.resize((120,40),Image.ANTIALIAS)
        self.pict2=ImageTk.PhotoImage(img2)
        log_btn=Button(frame,image=self.pict2,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'),bg='white')
        log_btn.place(x=340,y=420,width=180)





if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()