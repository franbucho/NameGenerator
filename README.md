
# Generador de Nombres de Empresas

Este es un simple generador de nombres de empresas que utiliza la API de OpenAI (GPT-3) para generar nombres basados en palabras clave proporcionadas por el usuario. La aplicación tiene una interfaz gráfica desarrollada con tkinter en Python.

## Requisitos

- Python 3.x instalado en tu sistema.
- Las bibliotecas `requests` y `tkinter` instaladas. Puedes instalarlas ejecutando:

    ```bash
    pip install requests tkinter
    ```

## Uso

1. Clona o descarga este repositorio en tu máquina local.

2. Obtén tu clave de API de OpenAI:
   - Regístrate en [OpenAI](https://platform.openai.com/signup) para obtener acceso a la API.
   - Crea un archivo llamado `.env` en el directorio raíz del proyecto.
   - Dentro de `.env`, guarda tu clave de API de OpenAI de la siguiente manera:

        ```
        OPENAI_API_KEY=YOUR_API_KEY_HERE
        ```

3. Ejecuta la aplicación:

    ```bash
    python main.py
    ```

4. En la ventana de la aplicación:
   - Ingresa al menos tres nombres de empresas que te interesen en el campo de entrada.
   - Haz clic en el botón "Generar Nombre" para obtener variaciones de estos nombres.

## Funcionalidades

- **Generación de Nombres:** El usuario puede ingresar al menos tres nombres de empresas en el campo de entrada. Al hacer clic en el botón "Generar Nombre", se generarán variaciones de estos nombres utilizando la API de OpenAI.

- **Visualización de Nombres Generados:** Los nombres generados se mostrarán en un área de texto dentro de la ventana de la aplicación. Puedes desplazarte hacia abajo para ver todos los nombres generados.

## Ejemplo de Código

Aquí hay un ejemplo de cómo se puede mejorar el código para permitir que el usuario elija al menos tres nombres y obtener variaciones de ellos:

```python
import requests
import tkinter as tk
from tkinter import scrolledtext

def generar_variaciones():
    nombres = entry.get().split(",")
    
    for nombre in nombres:
        url = "https://api.openai.com/v1/engines/davinci/completions"
        headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        }
        
        prompt = nombre.strip() + " para una empresa de"
        
        data = {
            "prompt": prompt,
            "max_tokens": 20
        }
        
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        
        nombre_generado = result['choices'][0]['text']
        nombres_generados.insert(tk.END, nombre_generado + "\n")

# Crear la ventana principal
window = tk.Tk()
window.title("Generador de Nombres de Empresas")

# Crear el campo de entrada y el botón
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

btn_generar = tk.Button(window, text="Generar Variaciones", command=generar_variaciones)
btn_generar.pack(pady=5)

# Crear el área de texto para mostrar los nombres generados
nombres_generados = scrolledtext.ScrolledText(window, width=60, height=10)
nombres_generados.pack(pady=10)

# Leer la clave de API desde el archivo .env
with open(".env", "r") as file:
    api_key = file.read().strip()

# Ejecutar la ventana
window.mainloop()
```

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz tus cambios y realiza un commit (`git commit -am 'Añade nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Agradecimientos

Este proyecto utiliza la API de OpenAI (GPT-3) para la generación de nombres de empresas.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

---

Puedes personalizar este README según tus necesidades específicas y los detalles de tu proyecto. Asegúrate de reemplazar `YOUR_API_KEY_HERE` con tu clave de API real en el archivo `.env`. Además, puedes añadir secciones adicionales, como información sobre cómo obtener una clave de API, cómo configurar el entorno, etc.

Espero que esto te ayude a tener un README básico para tu proyecto. ¡Buena suerte!
