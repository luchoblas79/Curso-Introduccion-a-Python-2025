#Generador de tickets por consola
# Este programa permite generar tickets de soporte técnico, guardarlos en archivos JSON y leer tickets existentes.
# El usuario puede crear un ticket ingresando su nombre, sector, asunto y problema.     
# Los tickets se guardan en un directorio llamado "tickets" y se almacenan en formato JSON.
# El usuario también puede leer tickets existentes ingresando el número del ticket.

import os
import json
import random

# Función para generar un ticket
def generar_ticket():   
    ticket = {}
    ticket['numero'] = random.randint(1000, 9999)
    ticket['nombre'] = input("Ingrese su nombre: ")
    ticket['sector'] = input("Ingrese su sector: ")
    ticket['asunto'] = input("Ingrese el asunto del ticket: ")
    ticket['problema'] = input("Describa el problema: ")
    
    print("\nTicket generado con éxito:")
    print(f"Número de Ticket: {ticket['numero']}")
    print(f"Nombre: {ticket['nombre']}")
    print(f"Sector: {ticket['sector']}")
    print(f"Asunto: {ticket['asunto']}")
    print(f"Problema: {ticket['problema']}\n")
    print("IMPORTANTE: Recuerde su número de ticket para futuras consultas.")
    print("\nSi desea crear otro ticket, seleccione la opción correspondiente en el menú principal.")
        
    return ticket

# Función para guardar el ticket en un archivo JSON
def guardar_ticket(ticket):
     
    filename = f'tickets/ticket_{ticket["numero"]}.json'
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(ticket, file, indent=4,ensure_ascii=False)   
    print(f"Ticket guardado en {filename}")

# Función para leer un ticket
def leer_ticket():
    numero_ticket = input("Ingrese el número del ticket que desea leer: ")
    filename = f'tickets/ticket_{numero_ticket}.json'
    
    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as file:
            ticket = json.load(file)
            print("\nTicket encontrado:")
            print(f"Número de Ticket: {ticket['numero']}")
            print(f"Nombre: {ticket['nombre']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Problema: {ticket['problema']}")    
    else:
        print("No se encontró un ticket con ese número.")   
    return 

#Funcion Salir
def salir():
    print("Gracias por usar el sistema de tickets. ¡Hasta luego!")
    exit()  

# Función principal del programa
def main():
    while True:
        print("\n^^^^^^ Bienvenidos al Sistema de tickets ^^^^^^\n")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            ticket = generar_ticket()
            guardar_ticket(ticket)
            continue

        elif opcion == '2':
            leer_ticket()
            continue  

        elif opcion == '3':
            salir()

        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutamos la función principal
main()      

