import requests
import tkinter as tk
from tkinter import scrolledtext, messagebox

def generar_nombres():
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    
    prompt = entry.get() + " para una empresa de"
    
    data = {
        "prompt": prompt,
        "max_tokens": 20
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    nombre = result['choices'][0]['text']
    nombres_generados.insert(tk.END, nombre + "\n")

def generar_variaciones():
    nombres_seleccionados = nombres_generados.get("1.0", tk.END).splitlines()
    
    if len(nombres_seleccionados) < 3:
        messagebox.showerror("Error", "Por favor selecciona al menos 3 nombres.")
        return
    
    variaciones_generadas.delete("1.0", tk.END)
    
    for nombre in nombres_seleccionados:
        for _ in range(3):  # Generar 3 variaciones por nombre
            variacion = nombre.lower().replace(" ", "-") + str(_)
            variaciones_generadas.insert(tk.END, variacion + "\n")

# Crear la ventana principal
window = tk.Tk()
window.title("Generador de Nombres de Empresas")

# Crear el campo de entrada y los botones
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

btn_generar = tk.Button(window, text="Generar Nombre", command=generar_nombres)
btn_generar.pack(pady=5)

btn_generar_variaciones = tk.Button(window, text="Generar Variaciones", command=generar_variaciones)
btn_generar_variaciones.pack(pady=5)

# Crear el área de texto para mostrar los nombres generados
nombres_generados = scrolledtext.ScrolledText(window, width=60, height=10)
nombres_generados.pack(pady=10)

# Crear el área de texto para mostrar las variaciones generadas
variaciones_generadas = scrolledtext.ScrolledText(window, width=60, height=10)
variaciones_generadas.pack(pady=10)

# Ejecutar la ventana
window.mainloop()
