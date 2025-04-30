import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from ICNITAS_funciones import calcular_altura, calcular_peso, determinar_epoca_geologica
from openpyxl import Workbook  # Importamos openpyxl

def calcular():
    """
    Calcula la altura, peso y época geológica del fósil.
    """
    tipo_fosil = tipo_fosil_var.get()
    try:
        longitud_huella = float(longitud_huella_var.get())
        profundidad_huella = float(profundidad_huella_var.get())
        distancia_entre_huellas = float(distancia_entre_huellas_var.get())
        antiguedad_huella = float(antiguedad_huella_var.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
        return

    # Validar el tipo de fósil
    if tipo_fosil not in ('dinosaurio_bipedo', 'dinosaurio_cuadrupedo', 'mamifero_fosil'):
        messagebox.showerror("Error", "Tipo de fósil no válido.")
        return

    altura = calcular_altura(longitud_huella, profundidad_huella, tipo_fosil)
    peso = calcular_peso(longitud_huella, profundidad_huella, tipo_fosil)
    epoca_geologica = determinar_epoca_geologica(antiguedad_huella)

    resultado_var.set(f"Altura: {altura:.2f} cm\nPeso: {peso:.2f} kg\nÉpoca geológica: {epoca_geologica}\nDistancia entre huellas: {distancia_entre_huellas:.2f} cm")

def exportar_resultados():
    """
    Exporta los resultados a un archivo Excel (.xlsx),
    agregando "cm" a las medidas de longitud y "M. A." a la antigüedad.
    """
    tipo_fosil = tipo_fosil_var.get()
    longitud_huella = longitud_huella_var.get()
    profundidad_huella = profundidad_huella_var.get()
    distancia_entre_huellas = distancia_entre_huellas_var.get()
    antiguedad_huella = antiguedad_huella_var.get()
    resultados = resultado_var.get()

    if not resultados or "Altura: nan" in resultados:  # Comprobar si hay resultados válidos
        messagebox.showerror("Error", "No hay resultados válidos para exportar.")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivo Excel", "*.xlsx")])
    if archivo:
        try:
            # Extraer los resultados individuales de la cadena
            partes = resultados.split('\n')
            altura = partes[0].split(': ')[1]
            peso = partes[1].split(': ')[1]
            epoca_geologica = partes[2].split(': ')[1]
            distancia_huellas = partes[3].split(': ')[1]

            # Crear un nuevo libro de Excel y seleccionar la hoja activa
            libro = Workbook()
            hoja = libro.active

            # Escribir la cabecera
            hoja.append(["Tipo de fósil", "Longitud de la huella (cm)", "Profundidad de la huella (cm)", "Distancia entre huellas (cm)",
                        "Antigüedad (M. A.)", "Altura (cm)", "Peso (kg)", "Época geológica"])

            # Escribir los datos, agregando "cm" a las medidas y "M. A." a la antigüedad
            hoja.append([tipo_fosil, longitud_huella + " cm", profundidad_huella + " cm", distancia_entre_huellas + " cm",
                        antiguedad_huella + " M. A.", altura, peso, epoca_geologica])

            # Guardar el libro
            libro.save(archivo)

            messagebox.showinfo("Éxito", f"Resultados exportados a {archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar los resultados: {e}")

def mostrar_ayuda():
    """
    Muestra un cuadro de diálogo con las instrucciones de uso.
    """
    ayuda_texto = (
        "Este programa calcula la altura, el peso y la época geológica de fósiles "
        "basándose en las huellas encontradas.\n\n"
        "Instrucciones:\n"
        "1. Selecciona el tipo de fósil del menú desplegable.\n"
        "2. Introduce la longitud de la huella en centímetros.\n"
        "3. Introduce la profundidad de la huella en centímetros.\n"
        "4. Introduce la distancia entre huellas en centímetros.\n"
        "5. Introduce la antigüedad de la huella en millones de años.\n"
        "6. Haz clic en 'Calcular' para obtener los resultados.\n"
        "7. Haz clic en 'Exportar' para guardar los resultados en un archivo Excel."
    )
    messagebox.showinfo("Ayuda", ayuda_texto)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cálculo de Parámetros de Fósiles")
root.geometry("400x500")

# Configurar el comportamiento de las filas y columnas al redimensionar la ventana
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(1, weight=1)

# Variables
tipo_fosil_var = tk.StringVar()
longitud_huella_var = tk.StringVar()
profundidad_huella_var = tk.StringVar()
distancia_entre_huellas_var = tk.StringVar()
antiguedad_huella_var = tk.StringVar()
resultado_var = tk.StringVar()

# Etiquetas y entradas
tk.Label(root, text="Tipo de fósil:").grid(row=0, column=0, pady=10, padx=10, sticky='w')
tipo_fosil_entry = ttk.Combobox(root, textvariable=tipo_fosil_var)
tipo_fosil_entry['values'] = ('dinosaurio_bipedo', 'dinosaurio_cuadrupedo', 'mamifero_fosil')
tipo_fosil_entry.grid(row=0, column=1, pady=10, padx=10, sticky='we')  # Expande horizontalmente
tipo_fosil_entry.current(0)  # Establecer el primer valor por defecto

tk.Label(root, text="Longitud de la huella (cm):").grid(row=1, column=0, pady=10, padx=10, sticky='w')
tk.Entry(root, textvariable=longitud_huella_var).grid(row=1, column=1, pady=10, padx=10, sticky='we')  # Expande horizontalmente

tk.Label(root, text="Profundidad de la huella (cm):").grid(row=2, column=0, pady=10, padx=10, sticky='w')
tk.Entry(root, textvariable=profundidad_huella_var).grid(row=2, column=1, pady=10, padx=10, sticky='we')  # Expande horizontalmente

tk.Label(root, text="Distancia entre huellas (cm):").grid(row=3, column=0, pady=10, padx=10, sticky='w')
tk.Entry(root, textvariable=distancia_entre_huellas_var).grid(row=3, column=1, pady=10, padx=10, sticky='we')  # Expande horizontalmente

tk.Label(root, text="Antigüedad (millones de años):").grid(row=4, column=0, pady=10, padx=10, sticky='w')
tk.Entry(root, textvariable=antiguedad_huella_var).grid(row=4, column=1, pady=10, padx=10, sticky='we')  # Expande horizontalmente

# Frame para los resultados
resultados_frame = tk.Frame(root)
resultados_frame.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

tk.Label(resultados_frame, text="Resultados:", anchor=tk.CENTER).pack(pady=(0, 5))  # Centrar "Resultados:"
tk.Label(resultados_frame, textvariable=resultado_var, justify=tk.LEFT).pack()  # Resultados debajo

# Frame para los botones
botones_frame = tk.Frame(root)
botones_frame.grid(row=7, column=0, columnspan=2, pady=10)  # Centrar los botones

# Botones dentro del Frame
tk.Button(botones_frame, text="Calcular", command=calcular).pack(side=tk.LEFT, padx=5)
tk.Button(botones_frame, text="Exportar", command=exportar_resultados).pack(side=tk.LEFT, padx=5)
tk.Button(botones_frame, text="Ayuda", command=mostrar_ayuda).pack(side=tk.LEFT, padx=5)

# Iniciar la aplicación
if __name__ == "__main__":
    root.mainloop()