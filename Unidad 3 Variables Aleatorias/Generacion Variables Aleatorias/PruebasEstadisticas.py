# Descripción: Prueba Chi-cuadrado con valores observados y esperados (Tkinter)
from scipy.stats import chisquare
import tkinter as tk

def realizar_prueba():
    # Se asegura que label_resultado es accesible dentro de la función
    global label_resultado
    
    observadas = [18,22,20]
    esperadas = [20,20,20]
    chi2, p = chisquare(observadas, f_exp=esperadas)
    
    label_resultado.config(text=f"Chi2={chi2:.2f}, p={p:.4f}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Prueba Estadística")

# Crear botón y label
tk.Button(ventana, text="Chi-cuadrado", command=realizar_prueba).pack(pady=10)
label_resultado = tk.Label(ventana, text="Resultado: ?")
label_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
