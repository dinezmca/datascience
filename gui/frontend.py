import tkinter as tk

root = tk.Tk()
root.title('Simple tkinter app')
root.geometry("200x100") # Note: use lowercase 'x' for geometry

def say_hello():
    print("Hello, World!")

hello_btn = tk.Button(root, text="Click me", command=say_hello)
hello_btn.pack(pady=20)

root.mainloop()
