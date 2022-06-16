from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title='Not found', message='No Data File Found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='No Details', message='No Details for the Website exists')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = ''.join(password_list) 

    password_entry.insert(END, generated_password)
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website.capitalize():{
            'email':email,
            'password':password
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Warning', message="Please make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?' )

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(pady=50, padx=50)



canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
# Entries
website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=40)
email_entry.insert(END, 't.muzeffer.1998@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)
# Buttons
search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text='Generate Password', command=password_generator)
generate_password_button.grid(column=2,row=3)

add_button = Button(text='Add', width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()