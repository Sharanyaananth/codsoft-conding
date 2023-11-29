import random
import string
import tkinter as tk

def generate_password(length):
    char= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password

def generate_and_display_password():
    password_length = int(length_entry.get())
    if password_length < 8:
       output.config(text="Password should be at least 8 characters long.")
    else:
        generated_password = generate_password(password_length)
        output.config(text="output: " + generated_password)


w = tk.Tk()
w.title("Password Generator")


length_label = tk.Label(w, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(w, width=60)
length_entry.pack()

button = tk.Button(w, text="create Password", command=generate_and_display_password)
button.pack()


output= tk.Label(w, text="", width=40, height=5, font=("Arial", 14))
output.pack()

w.mainloop()

