import simpy
import tkinter as tk

def inventario(env, salida, stock_inicial=10, punto_pedido=3, lote=5):
    stock = stock_inicial
    while True:
        yield env.timeout(1)
        stock -= 1
        salida.insert(tk.END, f"t={env.now}, stock={stock}\n")
        if stock <= punto_pedido:
            stock += lote
            salida.insert(tk.END, f"Reposición realizada. Nuevo stock={stock}\n")

def ejecutar():
    ventana = tk.Tk()
    ventana.title("Inventario")
    salida = tk.Text(ventana, height=15, width=50)
    salida.pack()
    env = simpy.Environment()
    env.process(inventario(env, salida))
    env.run(until=12)
    ventana.mainloop()

ejecutar()
