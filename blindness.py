from tkinter import *
from tkinter import messagebox
import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
import mysql.connector as sk
from matplotlib import pyplot as plt
from model import *
from PIL import ImageTk
print('GUI SYSTEM STARTED...')


def LogIn():
    username = box1.get()

    u = 1

    if len(username) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter something Sir")

    if u:
        password = box2.get()

        if len(password):
            query = "SELECT * FROM THEGREAT"

            sql.execute(query)

            data = sql.fetchall()

            g = 0
            b = 0

            for i in data:
                if i[0] == username:
                    g = 1
                if i[1] == password:
                    b = 1

            if g and b:
                messagebox.showinfo('Hello Sir', 'Welcome to the System')
            else:
                messagebox.showinfo('Sorry', 'Wrong Username or Password')

            global y
            y = True
        else:
            messagebox.showinfo("Error", "You must enter a password Sir!!")


def OpenFile():
    username = box1.get()
    if y:
        try:
            a = askopenfilename()
            value, classes = main(a)
            query = 'UPDATE THEGREAT SET PREDICT = "%s" WHERE USERNAME = "%s"' % (value, username)

            sql.execute(query)
            connection.commit()
            image = Image.open(a)
            file = image.convert('RGB')
            plt.imshow(np.array(file))
            plt.title(f'Your report says, Label : {value}, Class : {classes}')
            plt.show()
            print('Thanks for using the system !')
        except Exception as error:
            print("File not selected ! Exiting..., Please try again")


    else:
        messagebox.showinfo("Hello Sir", "You need to Login first")


x = 0
y = False


def Signup():
    username = box1.get()
    password = box2.get()

    u = 1

    if len(username) == 0 or len(password) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter something Sir")

    if u:
        query1 = "SELECT * FROM THEGREAT"
        sql.execute(query1)

        data = sql.fetchall()

        z = 1

        for i in data:
            if i[0] == username:
                messagebox.showinfo("Sorry Sir", "This  username is already registered, try a new one")
                z = 0

        if z:
            query = "INSERT INTO THEGREAT (USERNAME, PASSWORD) VALUES('%s', '%s')" % (username, password)
            messagebox.showinfo("signed up", ("Hi ", username, "\n Now you can login with your credentials !"))
            sql.execute(query)
            connection.commit()


connection = sk.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="DDR".lower()
)

sql = connection.cursor()

root = Tk()

root.geometry('960x638')
root.title("XAI model for Det_Dia_Ret")
#root.configure()
canvas = Canvas(width = 900, height = 400, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = "eye.jpg")
canvas.create_image(6, 6, image = image, anchor = NW)

label1 = Label(root, text="Det_Dia_Ret", font=('Arial', 30,'bold'), bg='#ffffff', fg='Black')
label1.place(x=300, y=30)

label2 = Label(root, text="Enter your username : ", font=('Arial', 12,'bold'), bg='#ffffff', fg='Black')
label2.place(x=120, y=150)

label3 = Label(root, text="Enter your password : ", font=('Arial', 12,'bold'), bg='#ffffff', fg='Black')
label3.place(x=120, y=200)

box1 = Entry(root)
box1.place(x=300, y=153)

box2 = Entry(root, show='*')
box2.place(x=300, y=203)

label4 = Label(root, text="or", font=('Arial', 12,'bold'), bg='#ffffff', fg='White')
label4.place(x=310, y=300)

button3 = Button(root, text="Sign Up", command=Signup)
button3.place(x=300, y=350)

button1 = Button(root, text="Log In", command=LogIn)
button1.place(x=300, y=250)

button2 = Button(root, text="Upload Image", command=OpenFile)
button2.place(x=500, y=250)

root.mainloop()
