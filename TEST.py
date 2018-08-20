import time as time
from tkinter import *
from tkinter import messagebox
import socket
from tkinter.filedialog import askopenfilename
import _thread
import os
from os.path import splitext
List= []
att = {}
AttList=[]
tk = Tk()
check = False
click = False
fileselected = False
def login():
    global user,password
    user = Entry(tk,bd = 5)
    password = Entry(tk,bd=5,show='*')
    userlabel= Label(tk,text='Username',)
    passlabel= Label(tk,text='Password')
    user.place(relx=0.5,rely=0.5)
    password.place(relx=0.5,rely=0.6)
    userlabel.place(relx=0.45,rely=0.5)
    passlabel.place(relx=0.45,rely=0.6)
    but = Button(tk, text='enter', command=check)
    but.place(relx=0.5,rely=0.7)
    tk.mainloop()

def check():
    global tk,check
    usercheck= user.get()
    passwordcheck= password.get()
    foo = usercheck + ':' + passwordcheck
    fo = open("Credentials.txt", "r")
    cred = fo.read()
    cred = cred.split("\n")
    if foo in cred:
        messagebox.showinfo('Login', 'Success!')
        tk.destroy()
        check = True
        startnetwork()
    else:
        messagebox.showinfo('', 'Username or Password is Incorrect')



def main():
    global entry,sock,host,port,client,addr
    if check == True:
        global entry,sock,host,port,client,addr
        main = Tk()
        entry= Text(main,bd=10)
        but = Button(main,bd=5,text='SEND',command=send)
        choosefilebut= Button(main,bd=2,text="Choose File",command=choosefile)
        choosefilebut.place(relx=0.75,rely=0.3)
        but.place(height=300,width=300,relx=0.7,rely=0.5)
        entry.place(height=400,width=400,relx=0.4,rely=0.5)

        main.mainloop()

    else:
        messagebox.showinfo('', 'Please login first')

def choosefile():
# TODO implement file sharing
    global fileobj,fileselected,extension,size
    filename= askopenfilename()
    filename,extension=splitext(filename)
    size= os.path.getsize(filename + extension)
    size= str(size)
    print(size)
    if extension==".JPG":
        fileobj = open(filename + extension, "rb")
        fileselected = True

    else:
        fileobj=open(filename + extension,"r")
        fileselected= True

def startnetwork():
    global sock,host,port,client,addr
    sock= socket.socket()
    host= socket.gethostname()
    port= 12345
    sock.bind((host,port))
    sock.listen(5)
    main()
def send():
    global client,fileselected
    try:
        if fileselected == True:
            client.send("FINCOMING".encode())
            client.send(extension.encode())
            if extension == ".JPG":
                client.send(fileobj.read())
            else:
                client.send(fileobj.read(1024).encode())
                fileselected=False

        msg = entry.get("1.0", END)
        client.send(msg.encode())


    except ConnectionResetError:
        messagebox.showinfo('','An existing connection was forcibly closed by the remote host')
        q = messagebox.askyesno('',"Search for new connection?")
        print(q)
        if q == True:
            connect()
    except NameError:
        messagebox.showinfo('', 'No connection detected. Checking for connection now')
        connect()

def connect():
    global client
    client, addr = sock.accept()
    print('Got connection from', addr)
    con = 'Connected to ' + str(host)
    client.send(con.encode())

while True:
    def run():
        try:
            com=input("command?")
            eval(com)
        except (SyntaxError,NameError):
            run()
    run()

