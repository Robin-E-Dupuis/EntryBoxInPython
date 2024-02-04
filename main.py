from tkinter import *

def submit():
    username = entry.get()
    print("Your username is "+username)
    password = entry1.get()
    print("Your password is " + password)
def delete():
    entry.delete(0, END)
    entry1.delete(0, END)
def backspace():
    entry.delete(len(entry.get())-1, END)
    entry1.delete(len(entry1.get()) - 1, END)

window = Tk()
window.config(background="pink")
window.geometry("700x200")

entry = Entry(window,  font=("Arial", 15), background="purple", fg="#00FF00")
entry.insert(0,'username')
entry.pack(side=LEFT)

entry1 = Entry(window,  font=("Arial", 15), background="purple", fg="#00FF00", show="*")
entry1.insert(0,'password')
entry1.pack(side=LEFT)

submit_button = Button(window,text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace = Button(window,text="backspace", command=backspace)
backspace.pack(side=RIGHT)
window.mainloop()
