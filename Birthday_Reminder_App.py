import datetime
from tkinter import *
from Important import display_birthday
from Important import add_birth
from Important import remove_birthday

Today_date = datetime.datetime.now()
Current_date = Today_date.strftime("%d %B %Y")

root = Tk()
root.geometry("400x350+500+150")
root.resizable(0, 0)
root.title("Birthday Reminder")
root.iconbitmap(r'./imgs/Birthday_logo.ico')
root.configure(bg='#ffffff')

Current_date1 = Label(text="Date: " + Current_date, font=("", 12, 'bold'), bg='#ffffff')
Current_date1.pack(anchor=NE, pady=8, padx=10, )
Show = Button(text="Show", font=("", 14, 'bold'), bd=10, command=display_birthday.display_window)
Add = Button(text="Add", font=("", 14, 'bold'), bd=10, command=add_birth.add_window)
Remove = Button(text="Remove", font=("", 14, 'bold'), bd=10, command=remove_birthday.remove_window)
Exit = Button(text="Exit", font=("", 14, 'bold'), bd=10, command=exit)

Show.pack(ipadx=25.3, pady=10)
Add.pack(ipadx=32.5, pady=10)
Remove.pack(ipadx=14, pady=10)
Exit.pack(ipadx=33.5, pady=10)

root.mainloop()
