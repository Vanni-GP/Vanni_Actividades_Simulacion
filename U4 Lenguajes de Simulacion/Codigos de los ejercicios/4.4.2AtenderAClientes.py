import simpy
import tkinter as tk
import random

def cliente(env, nombre, cajero, salida):
    llegada = env.now
    with cajero.request() as req:
        yield req
        espera = env.now - llegada
        tiempo = random.randint(1,5)
        yield env.timeout(tiempo)
        salida.insert(tk.END, f"{nombre}: espera={espera}, servicio={tiempo}\n")

def ejecutar():
    ventana = tk.Tk()
    ventana.title("Prueba No Paramétrica")
    salida = tk.Text(ventana, height=15, width=50)
    salida.pack()
    env = simpy.Environment()
    cajero = simpy.Resource(env, capacity=1)
    for i in range(5):
        env.process(cliente(env, f"Cliente {i+1}", cajero, salida))
    env.run()
    ventana.mainloop()

ejecutar()
