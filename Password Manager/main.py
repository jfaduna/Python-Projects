from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # fmt: off
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # fmt: on

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if "" in [website, username, password]:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        is_true = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\n Are you sure you want to save?",
        )
        if is_true:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Create a window using tkinter
# Add Title "Password Manager"
# width = 200, height = 200, padding = 20
# Add MyPass Logo in the center

WHITE = "#ffffff"
BLACK = "#000000"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

website_label = Label(text="Website:", bg=WHITE, fg=BLACK)
website_label.grid(column=0, row=1)
website_input = Entry(width=36, bg=WHITE, fg=BLACK, highlightbackground=WHITE)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK)
username_label.grid(column=0, row=2)
username_input = Entry(width=36, bg=WHITE, fg=BLACK, highlightbackground=WHITE)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "user@user.com")

password_label = Label(text="Password:", bg=WHITE, fg=BLACK)
password_label.grid(column=0, row=3)
password_input = Entry(width=19, bg=WHITE, fg=BLACK, highlightbackground=WHITE)
password_input.grid(column=1, row=3)

generate_password_button = Button(
    text="Generate Password",
    highlightbackground=WHITE,
    fg=BLACK,
    command=generate_password,
)
generate_password_button.grid(column=2, row=3)

add_button = Button(
    text="Add", width=34, highlightbackground=WHITE, fg=BLACK, command=save
)
add_button.grid(column=1, row=4, columnspan=2)

canvas = Canvas(height=200, width=200, bg=WHITE)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

window.mainloop()
