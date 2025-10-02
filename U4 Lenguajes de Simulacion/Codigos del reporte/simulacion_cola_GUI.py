# simulacion_cola_gui.py
import tkinter as tk
from tkinter import ttk
import simpy, random, statistics

def cliente(env, nombre, servidor, mean_service, wait_times, service_times):
    llegada = env.now
    with servidor.request() as req:
        yield req
        espera = env.now - llegada
        wait_times.append(espera)
        servicio = random.expovariate(1.0 / mean_service)
        service_times.append(servicio)
        yield env.timeout(servicio)

def generador_llegadas(env, servidor, mean_interarrival, mean_service, num_clientes, wait_times, service_times):
    for i in range(num_clientes):
        inter = random.expovariate(1.0 / mean_interarrival)
        yield env.timeout(inter)
        env.process(cliente(env, f"Cliente {i+1}", servidor, mean_service, wait_times, service_times))

def run_and_show():
    try:
        mean_interarrival = float(entry_interarrival.get())
        mean_service = float(entry_service.get())
        num_customers = int(entry_customers.get())
    except ValueError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Introduce valores válidos.\n")
        return

    random.seed(42)
    env = simpy.Environment()
    servidor = simpy.Resource(env, capacity=1)
    wait_times = []
    service_times = []
    env.process(generador_llegadas(env, servidor, mean_interarrival, mean_service, num_customers, wait_times, service_times))
    env.run()

    if wait_times:
        prom_espera = statistics.mean(wait_times)
        prom_serv = statistics.mean(service_times)
        prom_sistema = statistics.mean([w+s for w,s in zip(wait_times, service_times)])
        utilizacion = sum(service_times) / env.now
    else:
        prom_espera = prom_serv = prom_sistema = utilizacion = 0.0

    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Clientes simulados: {len(wait_times)}\n")
    text.insert(tk.END, f"Tiempo total sim: {env.now:.2f}\n")
    text.insert(tk.END, f"Promedio espera: {prom_espera:.3f} \n")
    text.insert(tk.END, f"Promedio servicio: {prom_serv:.3f}\n")
    text.insert(tk.END, f"Promedio en sistema: {prom_sistema:.3f}\n")
    text.insert(tk.END, f"Utilización servidor: {utilizacion:.3f}\n")

root = tk.Tk()
root.title("Simulación de Colas - SimPy (GUI)")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Media entre llegadas (min)").grid(column=0, row=0)
entry_interarrival = ttk.Entry(frm); entry_interarrival.insert(0, "5.0"); entry_interarrival.grid(column=1, row=0)
ttk.Label(frm, text="Media servicio (min)").grid(column=0, row=1)
entry_service = ttk.Entry(frm); entry_service.insert(0, "3.0"); entry_service.grid(column=1, row=1)
ttk.Label(frm, text="Clientes a simular").grid(column=0, row=2)
entry_customers = ttk.Entry(frm); entry_customers.insert(0, "50"); entry_customers.grid(column=1, row=2)
btn = ttk.Button(frm, text="Ejecutar simulación", command=run_and_show)
btn.grid(column=0, row=3, columnspan=2, pady=8)
text = tk.Text(frm, width=50, height=10); text.grid(column=0, row=4, columnspan=2)
root.mainloop()
