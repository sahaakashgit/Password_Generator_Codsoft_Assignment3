import tkinter as tk
import random
import string


def generate_password():
    password_length_str = length_entry.get()

    if not password_length_str.isdigit():
        result_label.config(
            text="Please enter a valid password length (a positive integer).",
            fg="red",
        )
        return

    password_length = int(password_length_str)
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    lowercase_chars = string.ascii_lowercase if include_lowercase else ""
    uppercase_chars = string.ascii_uppercase if include_uppercase else ""
    digit_chars = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special_chars else ""

    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    if not all_chars:
        result_label.config(
            text="Please select at least one character type.",
            fg="red",
        )
    else:
        password = "".join(random.choice(all_chars) for _ in range(password_length))
        result_label.config(
            text=f"Generated Password: {password}",
            fg="green",
        )


window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg="Black")


length_label = tk.Label(
    window, text="Password Length:", bg="Black", fg="white", font=("Arial", 12)
)
length_entry = tk.Entry(window, font=("Arial", 12))
lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(
    window,
    text="Include Lowercase Letters",
    variable=lowercase_var,
    bg="Black",
    fg="white",
    font=("Arial", 12),
    selectcolor="red",
)
uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(
    window,
    text="Include Uppercase Letters",
    variable=uppercase_var,
    bg="Black",
    fg="white",
    font=("Arial", 12),
    selectcolor="red",
)
digits_var = tk.IntVar()
digits_check = tk.Checkbutton(
    window,
    text="Include Digits",
    variable=digits_var,
    bg="Black",
    fg="white",
    font=("Arial", 12),
    selectcolor="red",
)
special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(
    window,
    text="Include Special Characters",
    variable=special_chars_var,
    bg="Black",
    fg="white",
    font=("Arial", 12),
    selectcolor="red",
)
generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password,
    bg="#41679a",
    fg="white",
    font=("Arial", 12),
)
result_label = tk.Label(window, text="", font=("Arial", 12), bg="black", wraplength=300)


length_label.pack(pady=10)
length_entry.pack(pady=5)
lowercase_check.pack()
uppercase_check.pack()
digits_check.pack()
special_chars_check.pack()
generate_button.pack(pady=10)
result_label.pack()


window.mainloop()
