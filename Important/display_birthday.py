from tkinter import *from tkinter import messageboxfrom Important.main_program import *def display_window():    def selected():        name = display_birth_list_box.get(ACTIVE)        date = userId.friend_birth.get(name)        messagebox.showinfo(f"More about {name}", "Name of person:- " + name + "\nDate of birth:- " + date)        root.destroy()        display_window()    def back():        root.destroy()    root = Tk()    root.geometry("400x350+500+150")    root.resizable(0, 0)    root.title("See Birthday")    root.iconbitmap(r'./imgs/Birthday_logo.ico')    root.configure(bg='#ffffff')    my_fram = Frame(root)    my_fram.pack(fill="both", expand=True)    sbr = Scrollbar(my_fram, )    sbr.pack(side=RIGHT, fill=Y)    display_birth_list_box = Listbox(my_fram, bg='#ffffff', font=("", 14, 'bold'))    display_birth_list_box.pack(side=LEFT, fill="both", expand=True)    display_birth_ = Label(my_fram, bg='#ffffff', font=("", 14, 'bold'))    display_birth_.pack(side=LEFT, fill="both", expand=True)    sbr.config(command=display_birth_list_box.yview)    display_birth_list_box.config(yscrollcommand=sbr.set)    show_btn = Button(root, text="Show more", command=selected, font=("", 16, 'bold'))    show_btn.pack(fill=X, side=BOTTOM)    cancel_btn = Button(root, text="Back", font=("", 16, 'bold'), command=back)    cancel_btn.pack(fill=X, side=BOTTOM)    if userId.friend_birth == {}:        display_birth_list_box.destroy()        sbr.destroy()        show_btn.destroy()        display_birth_.config(text="NOT ADDED ANY BIRTHDAYS")    else:        display_birth_.destroy()        for friend, birthdate in userId.friend_birth.items():            display_birth_list_box.insert(1, f"{friend}")    root.mainloop()