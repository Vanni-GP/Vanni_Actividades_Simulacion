# Descripción: Combina dos distribuciones
import random
import tkinter as tk

def generar_composicion():
    u = random.random()
    x = random.random()*2 if u<0.3 else 2 + random.random()*3
    label_resultado.config(text=f"Variable por composición: {x:.4f}")

ventana = tk.Tk()
ventana.title("Composición")
tk.Button(ventana, text="Generar", command=generar_composicion).pack()
label_resultado = tk.Label(ventana, text="Variable por composición: ?")
label_resultado.pack()
ventana.mainloop()
