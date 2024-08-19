import tkinter as tk
from tkinter import ttk

def fade_in(window, duration):
    alpha = window.attributes('-alpha')
    step = 1.0 / (duration * 10)

    def update_alpha():
        nonlocal alpha
        alpha += step
        window.attributes('-alpha', alpha)
        if alpha < 1:
            window.after(100, update_alpha)

    update_alpha()

def main():
    root = tk.Tk()
    root.title("Fade In Example")
    root.geometry("300x100")

    label = ttk.Label(root, text="Ryani, eu perdi tua pasta kkkkk faz o LLLLL", font=("Helvetica", 14))
    label.pack(pady=20)

    root.attributes('-alpha', 0.0)  # Set initial alpha to 0 for fade in effect

    fade_in(root, 2)  # Duration of fade in effect in seconds

    root.mainloop()

if __name__ == "__main__":
    main()
