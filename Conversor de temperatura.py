# Nota: Este código crea una ventana de conversión de temperatura simple que permite al usuario ingresar una temperatura 
# y convertirla entre Celsius y Fahrenheit.     
# El resultado se muestra en la misma ventana.
# Se utiliza la biblioteca tkinter para crear la interfaz gráfica de usuario.   
# El usuario puede seleccionar la conversión deseada mediante un menú desplegable.
# El botón "Convertir" realiza la conversión y muestra el resultado en una etiqueta.   


import tkinter as tk

def es_numero(val):
    val = val.strip().replace('.', '', 1).replace('-', '', 1)
    return val.isdigit()

def convertir_temperatura():
    texto = entrada_temp.get()
    if not es_numero(texto):
        resultado.set("ERROR!Ingrese un número válido.")
        return

    temp = float(texto)
    if opcion.get() == "Celsius a Fahrenheit":
        resultado.set(f"{temp * 9/5 + 32:.2f} °F")
    else:
        resultado.set(f"{(temp - 32) * 5/9:.2f} °C")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("300x400")
ventana.resizable(False, False)
ventana.configure(background="#1C1D1D")


etiqueta_temp = tk.Label(ventana, text="Ingrese la temperatura:", font=("Arial", 14), bg="#1C1D1D", fg="#FFFFFF")
etiqueta_temp.pack()    

entrada_temp = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada_temp.pack(pady=10)

etiqueta_conversion = tk.Label(ventana, text="Seleccione la conversión:", font=("Arial", 14), bg="#1C1D1D", fg="#FFFFFF")
etiqueta_conversion.pack(pady=10)

# Menú desplegable
opcion = tk.StringVar(value="Celsius a Fahrenheit")
opciones = tk.OptionMenu(ventana, opcion, "Celsius a Fahrenheit", "Fahrenheit a Celsius")
opciones.config(font=("Arial", 14), bg="#94F880", fg="#000000")
opciones.pack(pady=10)

# Botón de conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_temperatura, font=("Arial", 14), bg="#1572C9", fg="#000000")
boton_convertir.pack(pady=10)

# Resultado
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 14), bg="#1C1D1D", fg="#FFFFFF")
etiqueta_resultado.pack(pady=10)

# Bucle principal
ventana.mainloop()
 
