# Descripción: Variable aleatoria exponencial usando transformada inversa
import random
import math
import tkinter as tk

def generar_transformada():
    u = random.random()
    x = -math.log(1-u)
    label_resultado.config(text=f"Transformada inversa: {x:.4f}")

ventana = tk.Tk()
ventana.title("Transformada Inversa")
tk.Button(ventana, text="Generar", command=generar_transformada).pack()
label_resultado = tk.Label(ventana, text="Transformada inversa: ?")
label_resultado.pack()
ventana.mainloop()
