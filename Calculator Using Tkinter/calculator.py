import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + button_text)

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x400")
root.configure(bg="#000000")  # Black background

# Entry widget to display expressions
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify='right', bg="#1e1e1e", fg="white")
entry.pack(pady=10, padx=10, fill="both")

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons
button_frame = tk.Frame(root, bg="#000000")
button_frame.pack()
for row in buttons:
    button_row = tk.Frame(button_frame, bg="#000000")
    button_row.pack()
    for char in row:
        button = tk.Button(button_row, text=char, font=("Arial", 18), width=5, height=2, bg="#007BFF", fg="white", bd=3, relief="raised", command=lambda ch=char: on_click(ch))
        button.pack(side="left", padx=5, pady=5)

# Run the application
root.mainloop()