import random
import tkinter as tk
from tkinter import messagebox

def generar():
    entero = random.randint(0, 99)
    decimal = random.random()
    mensaje = f"Número entero aleatorio: {entero}\nNúmero decimal aleatorio: {decimal}"
    messagebox.showinfo("Resultados", mensaje)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generación Aleatoria")
ventana.geometry("300x200")

# Botón para generar números
boton = tk.Button(ventana, text="Generar números", command=generar, font=("Arial", 12))
boton.pack(expand=True)

# Ejecutar ventana
ventana.mainloop()
