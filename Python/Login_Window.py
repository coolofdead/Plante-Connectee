from tkinter import *
from time import sleep

"------------------------- FUNCTIONS -------------------------------"
def Login(evt=None):
    username = username_entry.get()
    password = password_entry.get()
    
    loading_label.config(text="loading...")
    loading_label.place(relx=0.5, rely=0.55, anchor=CENTER)
    
    from main import Connection
    global window
    Logged(Connection(username, password))

def Logged(logs):
    loading_label.config(text=logs)
    loading_label.place(relx=0.5, rely=0.55, anchor=CENTER)
    loading_label.after(3000, loading_label.place_forget)
    
    global window
    if(logs == "succes"):
        window.destroy()
        from Device_Window import OpenWindow as OpenDeviceWindow
        OpenDeviceWindow()

def OpenWindow():
    global window
    window = Tk()
    window.minsize(400, 300)
    window.bind("<Return>", Login)
    window.wm_title("Login")
    window.resizable(0,0)

    username_label = Label(window, anchor=CENTER, text="Username :")
    username_label.place(relx=0.3, rely=0.3, anchor=CENTER)

    global username_entry
    username_entry = Entry(window)
    username_entry.place(relx=0.55, rely=0.3, anchor=CENTER)

    password_label = Label(window, text="Password :")
    password_label.place(relx=0.3, rely=0.4, anchor=CENTER)

    global password_entry
    password_entry = Entry(window)
    password_entry.config(show="*")
    password_entry.place(relx=0.55, rely=0.4, anchor=CENTER)

    login_button = Button(window, text="login", command=Login)
    login_button.config(width=10, height=2)
    login_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    global loading_label
    loading_label = Label(window, text="loading...")
