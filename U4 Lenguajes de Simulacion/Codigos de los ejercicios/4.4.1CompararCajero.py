import simpy
import tkinter as tk

def cliente(env, nombre, cajero, salida):
    llegada = env.now
    with cajero.request() as req:
        yield req
        espera = env.now - llegada
        yield env.timeout(4)
        salida.insert(tk.END, f"{nombre} esperó {espera}\n")

def simular(capacidad, salida):
    env = simpy.Environment()
    cajero = simpy.Resource(env, capacity=capacidad)
    for i in range(5):
        env.process(cliente(env, f"Cliente {i+1}", cajero, salida))
    env.run()

def ejecutar():
    ventana = tk.Tk()
    ventana.title("Prueba Paramétrica")
    salida = tk.Text(ventana, height=15, width=50)
    salida.pack()
    salida.insert(tk.END, "Simulación con 1 cajero:\n")
    simular(1, salida)
    salida.insert(tk.END, "\nSimulación con 2 cajeros:\n")
    simular(2, salida)
    ventana.mainloop()

ejecutar()
