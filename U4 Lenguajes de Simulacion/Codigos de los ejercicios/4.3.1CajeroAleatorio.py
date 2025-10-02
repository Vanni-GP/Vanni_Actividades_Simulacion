import simpy
import tkinter as tk
import random

def cliente(env, nombre, cajero, salida):
    llegada = env.now
    with cajero.request() as req:
        yield req
        espera = env.now - llegada
        tiempo = random.randint(2,5)
        yield env.timeout(tiempo)
        salida.insert(tk.END, f"{nombre} esperó {espera} y tardó {tiempo}\n")

def ejecutar():
    ventana = tk.Tk()
    ventana.title("Cola de Clientes")
    salida = tk.Text(ventana, height=10, width=40)
    salida.pack()
    env = simpy.Environment()
    cajero = simpy.Resource(env, capacity=1)
    for i in range(5):
        env.process(cliente(env, f"Cliente {i+1}", cajero, salida))
    env.run()
    ventana.mainloop()

ejecutar()
