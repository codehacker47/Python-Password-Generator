import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    characters = ""
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if characters == "":
        password_label.config(text="Select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated password: {password}")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Lenght of password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")  

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
uppercase_checkbox.pack()

lowercase_checkbox = tk.Checkbutton(root, text="Include downcase letters", variable=lowercase_var)
lowercase_checkbox.pack()

numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_checkbox.pack()

special_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_var)
special_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()