from tkinter import *
from tkinter import messagebox
import random

def no():
    if messagebox.askyesno(title='confirmation', message='u sure?'):
        messagebox.showinfo(' ', 'ok u gay, thanks bro')
    else:
        messagebox.showinfo(' ', 'sike too late, haha u gay now')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'black'

label = Label(root, text='Are you gay?', font='Arial 20 bold', bg='black').pack()
btnYes = Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Yes', font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()
