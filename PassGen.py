import random
from tkinter import *
import pyperclip

root = Tk()

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]},;.-/\\+_$#@!^&*"

all = uppercase_letters + lowercase_letters + digits + symbols

character_label = Label(root, text="Number Of Characters", font=("Arial, 12"), bg="#77acde").pack(padx=10)
all_length = Entry(root, font="Arial 14", bg="#96bee5")
all_length.pack(padx=10)
    
    
def generate_pass():
    length = all_length.get()
    password = "".join(random.sample(all, int(length)))
    print(password)
    label_pass.config(text="Generated Pass: " + password + " Text has been copied ")
    pyperclip.copy(password)
    

Button(root, text="Generate Password", command=generate_pass, font=("Arial 14"), bg="#5382af").pack(padx=10)
label_pass = Label(root, font=("Arial, 12"), bg="#5d92c5")
label_pass.pack()

root.config(background="#68A3DB")
root.geometry("400x200")
root.resizable(True, False)
root.title("Password Generator")
root.mainloop()