from tkinter import *
from random import randint

root = Tk()
root.title('KN - Secure Password Generator')
root.geometry("500x300")


def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(user_entry.get())
    user_password = ''
    for i in range(pw_length):
        user_password += chr(randint(33,126))
    pw_entry.insert(0, user_password)

def copy():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Create label frame 
char_frame = LabelFrame(root, text="How Many Characters?")
char_frame.pack(pady=20)

# Create entry box for user to enter desired number of characters
user_entry = Entry(char_frame, font=("Helvetica, 24"))
user_entry.pack(pady=20, padx=20)

# Create entry box for generated password
pw_entry = Entry(root, text='', font=("Helvetica, 24"), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create frame for buttons
buttons_frame = Frame(root)
buttons_frame.pack(pady=20)

# Create buttons
gen_button = Button(buttons_frame, text="Generate Secure Password", command=new_rand) 
gen_button.grid(row=0, column=0, padx=10)

copy_button = Button(buttons_frame, text="Copy to Clipboard", command=copy) 
copy_button.grid(row=0, column=1, padx=10)

root.mainloop()