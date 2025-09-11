# Descripción: Aproxima N(0,1) con suma de 12 números uniformes
import random
import tkinter as tk

def generar_convolucion():
    suma = sum(random.random() for _ in range(12))
    normal = suma - 6
    label_resultado.config(text=f"Variable por convolución: {normal:.4f}")

ventana = tk.Tk()
ventana.title("Convolución")
tk.Button(ventana, text="Generar", command=generar_convolucion).pack()
label_resultado = tk.Label(ventana, text="Variable por convolución: ?")
label_resultado.pack()
ventana.mainloop()
