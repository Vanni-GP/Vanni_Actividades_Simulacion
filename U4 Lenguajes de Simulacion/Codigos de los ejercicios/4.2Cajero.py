import simpy
import tkinter as tk

def cliente(env, nombre, cajero, salida):
    with cajero.request() as req:
        yield req
        salida.insert(tk.END, f"{nombre} atendido en t={env.now}\n")
        yield env.timeout(5)

def ejecutar():
    ventana = tk.Tk()
    ventana.title("Simulación Cajero")
    salida = tk.Text(ventana, height=10, width=40)
    salida.pack()
    env = simpy.Environment()
    cajero = simpy.Resource(env, capacity=1)
    for i in range(10):
        env.process(cliente(env, f"Cliente {i+1}", cajero, salida))
    env.run()
    ventana.mainloop()

ejecutar()
