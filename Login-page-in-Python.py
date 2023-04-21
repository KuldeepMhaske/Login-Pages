from tkinter import *


def Login():
    print("Login Sucessfully...")


def Logout():
    print("Logout Sucessfully...")


def Signup():
    base1.mainloop()
    base1.destroy()


base1 = Tk()
base1.title("Login Form")
base1.geometry("1000x700")
base1.configure(bg="black")

header = Label(base1,text="Login Form",font=50,height=4,fg='white',bg='black')
header.pack()

text1 = Label(base1,text="Enter Email or Phone: ",fg='white',bg='black')
text1.place(x = 340, y = 110)

inputBox = Entry(base1,font=20,border=0)
inputBox.place(x = 500,y = 110)

text2 = Label(base1,text="Enter Password: ",fg = "white",bg='black')
text2.place(x = 340, y = 150)

inputBox1 = Entry(base1,font=20,show="*",border=0)
inputBox1.place(x = 500,y = 150)

btn = Button(base1,text = "Submit",bg='#0d6efd',fg='white', command=Login)
btn.place(x = 350,y = 230,height=50,width=150)

btn = Button(base1,text = "Reset",bg='#198754',fg='white',command=Logout)
btn.place(x = 530,y = 230,height=50,width=150)

btn5 = Button(base1,text = "New User?",fg='Black',command=Signup)
btn5.place(x = 440,y = 300,height=50,width=150)


base1.mainloop()