import tkinter as tk
from tkinter import messagebox

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Button frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=calculate)
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="Clear", width=20, height=2,
                      font=("Arial", 14), command=clear)
clear_btn.pack(pady=10)

root.mainloop()