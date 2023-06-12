# Agenda Precargada.

c1 = {"Celular": "+569922332", "Fono2": "5553322", "Mail": "juanPerez@yahoo", "Direccion": "Santiago"}
c2 = {"Celular": "+569943332", "Fono2": "5534432", "Mail": "juanCarcamo@yahoo", "Direccion": "Concepción"}
c3 = {"Celular": "+569964332", "Fono2": "2338932", "Mail": "juanSoto@yahoo", "Direccion": "Valdivia"}
c4 = {"Celular": "+569984332", "Fono2": "4442332", "Mail": "andresSoto@yahoo", "Direccion": "Santiago"}

agenda = {"Juan Perez": c1, "Juan Carcamo": c2, "Juan Soto": c3, "Andres Soto": c4}

# Funciones sin retorno, por desición de diseño.

def listar_contactos(agenda): # Entrega los Contactos Ordenados
    print("Estos son los Contactos Registrado: ")
    keys = agenda.keys() # Keys para ordenar los nombres.
    sorted_keys = sorted(keys) # Keys ordenas
    for e in sorted_keys:
        print("Nombre: ", e)
        print(agenda.get(e),"\n")
    
def cantidad_contacto(agenda): # Entrega la cantidad de contactos en la agenda.
    i = 0
    for e in agenda:
        i += 1
    print("Actualmente hay: ", i, "Contactos")
        
def buscar_contactos(agenda): # Entrega el nombre o parte del nombre
    buscar = input("Ingresa nombre o parte del nombre: ")
    keys =  sorted(agenda.keys()) # Keys ordenadas 
    lista_keys = [x for x in keys if buscar in x] # Lista por Compresión
    i = 1 # Entrega un índice de listado
    for e in lista_keys:
        print(i, e) 
        i +=1
        
def ver_contacto(agenda): # Entrega los datos de un contacto por nombre exacto
    contacto = input("Ingrese el contacto a mostrar por nombre exacto: ")
    print(agenda.get(contacto))

def crear_contacto(agenda): # Crea un contacto y se guarda en la agenda
    nombre = input("Ingrese el Nombre: ")
    celular = input("Ingrese el Número Celular: ")
    fono = input("Ingrese el Fono: ")
    mail = input("Ingrese el Mail: ")
    direccion = input("Ingrese la Dirección: ")
    
    contacto_nuevo = {"Celular": celular,"Fono2": fono, "Mail": mail, "Direccion": direccion}
    agenda[nombre] = contacto_nuevo
    print("Contacto agregado exitosamente")
    
def eliminar_contacto(agenda): # Elimina un contacto por nombre exacto
    eliminar = input("Contacto a eliminar por nombre exacto: ")
    agenda.pop(eliminar)   
    
print("Agenda de Contactos Python")
print("--------------------------")
print("Opciones: (1) Listar (2) Cantidad de Contactos (3) Buscar (4) Ver Contacto (5) Eliminar (6) Nuevo Contacto (7) Salir")
opcion = int(input("Ingrese su Opción: "))

while opcion != 7:
    
    if opcion == 1:
        listar_contactos(agenda)
        
    elif opcion == 2:
        cantidad_contacto(agenda)
        
    elif opcion == 3:
        buscar_contactos(agenda)
        
    elif opcion == 4:
        ver_contacto(agenda)
    
    elif opcion == 5:
        eliminar_contacto(agenda)
        
    elif opcion == 6:
        crear_contacto(agenda)
        
    else:
        print("Error en el Ingreso del la Opción")
    
    print("\nOpciones: (1) Listar (2) Cantidad de Contactos (3) Buscar (4) Ver Contacto (5) Eliminar (6) Nuevo Contacto (7) Salir")
    opcion = int(input("Ingrese su Opción: "))
        
print("Gracias por utilizar la agenda python")