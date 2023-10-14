from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = "Arial"
EMAIL = "situalex123@gmail.com"
# ---------------------------- Search Password ------------------------------- #
def search_password():
    website = website_box.get().lower()
    email = email_box.get()
    password = password_box.get()

    with open(r"E:\Python projects\Password manager\passwords.json", "r") as file:
        passwords = json.load(file)
        try:
            messagebox.showinfo(title=website, message=f"Email/Username: {passwords[website]['email']}\n           Password: {passwords[website]['password']}")
        except KeyError:
            messagebox.showinfo(title="Error", message="The website you searched for doesn't exist in the database")
            print(passwords[website]["email"])
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_box.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_generated = "".join(password_list)
    pyperclip.copy(password_generated)
    password_box.insert(END, string=password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    # entries are saved as strings
    website = website_box.get().lower()
    email = email_box.get()
    password = password_box.get()
    new_data = {website: {
                    "email": email,
                    "password": password}
    }
    if len(email_box.get()) == 0 or len(website_box.get()) == 0 or len(password_box.get()) == 0:
        messagebox.showinfo(title="DONT DO THAT I WILL FIND YOU", message="Don't leave any fields empty :)")

    if len(website_box.get()) != 0 and len(email_box.get()) != 0 and len(password_box.get()) != 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            # all entries are stored in an array
            with open(r"E:\Python projects\Password manager\passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open(r"E:\Python projects\Password manager\passwords.json", "w") as file:
                json.dump(data, file, indent=4)

            # clear entry box entries
            website_box.delete(0, END)
            password_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.minsize(width=200, height=200)
window.config(padx=40, pady=40)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file=r"E:\Python projects\Password manager\logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:", font=(FONT, 12), pady=10)
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:", font=(FONT, 12), pady=10)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=(FONT, 12), pady=10, padx=10)
password_label.grid(row=3, column=0)


# Entries
website_box = Entry(width=21, font=(FONT, 12))
website_box.place(in_=website_label, relx=1, x=38, y=10)
website_box.focus()

email_box = Entry(width=35 , font=(FONT, 12))
email_box.grid(row=2, column=1, columnspan=2)
email_box.insert(END, EMAIL)

password_box = Entry(width=21, font=(FONT, 12))

password_box.place(in_=password_label, relx=1, x=21, y=10)

# Buttons
generate_button = Button(text="Generate Password", font=(FONT, 8), justify="left", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=(FONT, 12), width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", font=(FONT, 8), justify="left", command=search_password, width= 16)
search_button.grid(row=1, column=2)


window.mainloop()