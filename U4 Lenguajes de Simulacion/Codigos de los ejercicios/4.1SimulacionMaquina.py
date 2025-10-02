import simpy
import tkinter as tk

def fabricar(env, salida):
    contador = 0
    while True:
        yield env.timeout(3)
        contador += 1
        salida.insert(tk.END, f"Pieza {contador} terminada en t={env.now}\n")

def ejecutar():
    ventana = tk.Tk()
    ventana.title("Simulación Máquina")
    salida = tk.Text(ventana, height=10, width=40)
    salida.pack()
    env = simpy.Environment()
    env.process(fabricar(env, salida))
    env.run(until=10)
    ventana.mainloop()

ejecutar()
