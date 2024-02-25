import requests
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def generar_variaciones(nombre):
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    
    variaciones = []
    
    for i in range(3):
        prompt = nombre + f" {i+1}"
        data = {
            "prompt": prompt,
            "max_tokens": 10
        }
        
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        variacion = result['choices'][0]['text']
        variaciones.append(variacion)
    
    return variaciones

def generar_nombres():
    nombre_base = entry.get()
    
    if not nombre_base:
        messagebox.showwarning("Advertencia", "Por favor ingresa al menos un nombre base.")
        return
    
    nombres = []
    
    for i in range(3):
        variaciones = generar_variaciones(nombre_base)
        nombres.append(nombre_base + f" {i+1}")
        nombres.extend(variaciones)
    
    for nombre in nombres:
        nombres_generados.insert(tk.END, nombre + "\n")

def cambiar_modo():
    if dark_mode.get():
        window.config(bg="black")
        entry.config(bg="black", fg="white")
        nombres_generados.config(bg="black", fg="white")
        dark_mode_switch.config(bg="black", fg="white", activebackground="black", activeforeground="white")
    else:
        window.config(bg="white")
        entry.config(bg="white", fg="black")
        nombres_generados.config(bg="white", fg="black")
        dark_mode_switch.config(bg="white", fg="black", activebackground="white", activeforeground="black")

# Crear la ventana principal
window = tk.Tk()
window.title("Generador de Nombres de Empresas")

# Configurar el modo oscuro
dark_mode = tk.BooleanVar()
dark_mode_switch = tk.Checkbutton(window, text="Modo Oscuro", variable=dark_mode, command=cambiar_modo)
dark_mode_switch.pack()

# Crear el campo de entrada y el botón
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

btn_generar = tk.Button(window, text="Generar Nombres", command=generar_nombres)
btn_generar.pack(pady=5)

# Crear el área de texto para mostrar los nombres generados
nombres_generados = scrolledtext.ScrolledText(window, width=60, height=10)
nombres_generados.pack(pady=10)

# Ejecutar la ventana
window.mainloop()
