from tkinter import *
import random
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '@', '$', '%', '&', '*', '+', '(', ')']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    digits_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += letters_list + digits_list + symbols_list
    random.shuffle(password_list)
    random_password = "".join(password_list)
    entry_password.insert(END, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = entry_website.get()
    user_name  = entry_username.get()
    password = entry_password.get()
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="some fields are empty. Please fill all the fields.")
    else:
        new_data = {website_name: {
            "email": user_name,
            "password": password
        }}
        try:
            with open("data.json", "r") as d_file:
                data = json.load(d_file)
        except FileNotFoundError:
            with open("data.json", "w") as d_file:
                json.dump(new_data, d_file, indent=4)
        else:
            data.update(new_data)       
            with open("data.json", "w") as d_file:
                json.dump(data, d_file, indent=4)
                # d_file.close()
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()
# ---------------------------- UI SETUP ------------------------------- #

win = Tk()
win.title("password manager")
win.config(padx=20, pady=20)
# win.minsize(width=400, height=400)
# win.maxsize(width=400, height=400)
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.focus()
entry_website.config(width=35)
entry_website.grid(column=1, row=1, columnspan=2)

label_username = Label(text="Email/Username: ")
label_username.grid(column=0, row=2)

entry_username = Entry()
entry_username.config(width=35)
entry_username.insert(END, "maspzaph@gmail.com")
entry_username.grid(column=1, row=2, columnspan=2)

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.config(width=21)
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password")
button_generate.config(command=generate_random_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add")
button_add.config(width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

win.mainloop()
