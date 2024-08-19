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

def show_message():
    message_label.config(text="Ta todinha aqui DENTRO DO MEU KURZINHO FAZUELIIII")

def main():
    root = tk.Tk()
    root.title("Fade In and Button Example")
    root.attributes('-fullscreen', True)  # Abre em tela cheia
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Define a geometria da tela cheia

    label = ttk.Label(root, text="Ryani, eu perdi tua pasta kkkkkkk", font=("Helvetica", 14))
    label.pack(pady=20)

    fade_in(root, 2)  # Duration of fade in effect in seconds

    message_button = ttk.Button(root, text="Clique aqui", command=show_message)
    message_button.pack(pady=10)

    global message_label
    message_label = ttk.Label(root, text="", font=("Helvetica", 14))
    message_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
