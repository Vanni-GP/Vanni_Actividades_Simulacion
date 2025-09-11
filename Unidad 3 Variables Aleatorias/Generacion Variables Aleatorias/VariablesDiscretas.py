import random
import tkinter as tk

def generar_dado():
    dado = random.randint(1,6)
    label_resultado.config(text=f"Dado: {dado}")

ventana = tk.Tk()
ventana.title("Variable Aleatoria Discreta")
tk.Button(ventana, text="Lanzar Dado", command=generar_dado).pack()
label_resultado = tk.Label(ventana, text="Dado: ?")
label_resultado.pack()
ventana.mainloop()
