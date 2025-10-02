import tkinter as tk
from tkinter import messagebox
import random

# Función para correr la simulación
def ejecutar_simulacion():
    try:
        inventario = int(entry_inventario.get())
        clientes = int(entry_clientes.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")
        return
    
    salida.delete("1.0", tk.END)
    for i in range(1, clientes + 1):
        demanda = random.randint(1, 5)
        salida.insert(tk.END, f"Cliente {i} llega y quiere {demanda} productos...\n")
        if inventario >= demanda:
            inventario -= demanda
            salida.insert(tk.END, f"-> Compra realizada. Productos entregados: {demanda}\n")
        else:
            salida.insert(tk.END, f"-> No hay suficiente inventario. Solo se entregaron {inventario}\n")
            inventario = 0
        salida.insert(tk.END, f"Inventario restante: {inventario}\n\n")
        if inventario == 0:
            salida.insert(tk.END, "⚠️ El inventario se ha agotado.\n")
            break
    
    salida.insert(tk.END, f"\n=== RESULTADOS FINALES ===\n")
    salida.insert(tk.END, f"Inventario final: {inventario}\n")
    salida.insert(tk.END, f"Clientes atendidos: {i}\n")
    salida.insert(tk.END, "Simulación terminada.\n")

# Crear ventana
ventana = tk.Tk()
ventana.title("Simulación de Inventario Interactiva")
ventana.geometry("500x500")

# Entradas de datos
tk.Label(ventana, text="Cantidad inicial de inventario:").pack()
entry_inventario = tk.Entry(ventana)
entry_inventario.pack()
entry_inventario.insert(0, "10")

tk.Label(ventana, text="Número de clientes:").pack()
entry_clientes = tk.Entry(ventana)
entry_clientes.pack()
entry_clientes.insert(0, "5")

# Botón para ejecutar
btn_ejecutar = tk.Button(ventana, text="Ejecutar Simulación", command=ejecutar_simulacion)
btn_ejecutar.pack(pady=10)

# Área de salida
salida = tk.Text(ventana, height=20, width=60)
salida.pack()

ventana.mainloop()
