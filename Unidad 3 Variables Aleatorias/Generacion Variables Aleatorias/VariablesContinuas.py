# Descripción: Genera un número decimal aleatorio y lo muestra en GUI
import random
import tkinter as tk

def generar_continuo():
    numero = random.random()
    label_resultado.config(text=f"Número continuo: {numero:.4f}")

ventana = tk.Tk()
ventana.title("Variable Aleatoria Continua")
tk.Button(ventana, text="Generar número", command=generar_continuo).pack()
label_resultado = tk.Label(ventana, text="Número continuo: ?")
label_resultado.pack()
ventana.mainloop()
