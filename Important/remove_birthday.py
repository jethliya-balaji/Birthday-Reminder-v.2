from tkinter import *
from tkinter import messagebox
from Important.main_program import *


def remove_window():
    def selected():
        old_data = pickle.load(open("data.pkl", "rb"))
        name = display_birth_list_box.get(ACTIVE)
        del userId.friend_birth[name]
        old_data.update(userId.friend_birth)
        pickle.dump(userId.friend_birth, open("data.pkl", "wb"))
        messagebox.showinfo("Removing...", name + " has been Removed Successfully")
        root.destroy()
        remove_window()

    def back():
        root.destroy()

    root = Tk()
    root.geometry("400x350+500+150")
    root.resizable(0, 0)
    root.iconbitmap(r'./imgs/Birthday_logo.ico')
    root.title("Remove Birthday")
    root.configure(bg='#000000')

    my_fram = Frame(root, )
    my_fram.pack(fill="both", expand=True)

    sbr = Scrollbar(my_fram, )
    sbr.pack(side=RIGHT, fill=Y)

    display_birth_list_box = Listbox(my_fram, bg='#ffffff', font=("", 14, 'bold'))
    display_birth_list_box.pack(side=LEFT, fill="both", expand=True)

    display_birth_ = Label(my_fram, bg='#ffffff', font=("", 14, 'bold'))
    display_birth_.pack(side=LEFT, fill="both", expand=True)

    cancel_btn = Button(root, text="Back", font=("", 16, 'bold'), command=back)
    cancel_btn.pack(fill=X, side=BOTTOM)
    remove_btn = Button(root, text="Remove", command=selected, font=("", 16, 'bold'))
    remove_btn.pack(fill=X, side=BOTTOM)

    sbr.config(command=display_birth_list_box.yview)
    display_birth_list_box.config(yscrollcommand=sbr.set)

    if userId.friend_birth == {}:
        display_birth_list_box.destroy()
        sbr.destroy()
        remove_btn.destroy()
        display_birth_.config(text="NOT ADDED ANY BIRTHDAYS")
    else:
        display_birth_.destroy()
        for friend, birthdate in userId.friend_birth.items():
            display_birth_list_box.insert(1, f"{friend}")

    root.mainloop()
