from tkinter import *
from random import randint

root = Tk()
root.title('KN - Secure Password Generator')
root.geometry("500x300")

user_password = chr(randint(33,126))

def new_rand():
    pass

def copy():
    pass

# Create label frame 
char_frame = LabelFrame(root, text="How Many Characters?")
char_frame.pack(pady=20)

# Create entry box for user to enter desired number of characters
user_entry = Entry(char_frame, font=("Helvetica, 24"))
user_entry.pack(pady=20, padx=20)

# Create entry box for generated password
pw_entry = Entry(root, text='', font="Helvetica, 24")
pw_entry.pack(pady=20)

# Create frame for buttons
buttons_frame = Frame(root)
buttons_frame.pack(pady=20)

# Create buttons
gen_button = Button(buttons_frame, text="Generate Secure Password", command=new_rand) 
gen_button.grid(row=0, column=0, padx=10)

copy_button = Button(buttons_frame, text="Copy to Clipboard", command=copy) 
copy_button.grid(row=0, column=0, padx=10)

root.mainloop()