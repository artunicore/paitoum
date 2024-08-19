import tkinter as tk

def desenhar_tetracirculos(canvas):
    raio = 30
    distancia = 60
    
    # Coordenadas do centro dos círculos
    coords = [
        (100, 100),
        (100 + distancia, 100),
        (100, 100 + distancia),
        (100 + distancia, 100 + distancia)
    ]

    for x, y in coords:
        canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill="blue")

def main():
    root = tk.Tk()
    root.title("Tetracírculos")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    desenhar_tetracirculos(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
