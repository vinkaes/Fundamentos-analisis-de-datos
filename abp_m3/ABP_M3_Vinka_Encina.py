 # Se crea clase Contacto
class Contacto:
    
    #Definición de la lista
    def __init__(self):
        self._datos = []
    
    # Método para agregar un nuevo contacto como diccionario en una lista
    def agregar_contacto(self):
        nombre = input("Ingresar nombre: ")
        telefono = input("Ingresar teléfono: ")  
        correo = input("Ingresar correo: ")
        direccion = input("Ingresar dirección: ")
        clientes = {"nombre": nombre, "telefono": telefono, "correo":correo,"direccion":direccion}
        self._datos.append(clientes)
        print("\033[1m_\033[0m"*70) 
        print()
    

    # Método para buscar un contacto segun nombre o teléfono
    def buscar_contacto(self): 
        dato_buscado= input("Ingrese el nombre o teléfono del contacto a buscar: ")
        encontrado = False
        for contacto_buscado in self._datos:
            
            if contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado:
               print(f"El contacto buscado es: {contacto_buscado}")
               encontrado = True
               break
        
        if not encontrado:
            print("Contacto no encontrado")
        
        print("\033[1m_\033[0m"*70) 
        print()
        return encontrado
        
        
    
    # Método para eliminar un contacto dado el nombre o teléfono de la persona a borrar
    def eliminar_contacto(self):
        dato_buscado= input("Ingrese el nombre o teléfono del contacto a eliminar: ")
        encontrado = False
        for contacto_buscado in self._datos:
            
            if contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado:
               self._datos.remove(contacto_buscado)
               print(f"\nContacto eliminado: {contacto_buscado}")
               print(f"\nContactos tras la eliminación: {self._datos}")
               encontrado = True
               break
        if not encontrado:
                 print("No se puede eliminar el contacto, el contacto no existe o fue mal ingresado el nombre o teléfono.")
        
        
        print("\033[1m_\033[0m"*70) 
        print()

    # Editar datos de contacto dado el nombre o teléfono de la persona a modificar
    def editar_contacto(self):
        dato_buscado = input("Ingrese el nombre o teléfono del contacto a editar: ")
        editar_nombre= input("Ingrese nuevo nombre o NO para no modificar dato: ")
        editar_telefono= input("Ingrese nuevo teléfono o NO para no modificar dato: ")
        editar_correo= input("Ingrese nuevo correo o NO para no modificar dato: ")
        editar_direccion= input("Ingrese nueva dirección o NO para no modificar dato: ")
        encontrado = False

        for contacto_buscado in self._datos:
            if (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono !="NO" and editar_correo !="NO" and editar_direccion !="NO":
                contacto_buscado.update({"nombre": editar_nombre,"telefono":editar_telefono,"correo":editar_correo,"direccion":editar_direccion})
                print(f"Resultado de edición: {contacto_buscado}")
                encontrado = True
                break

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono !="NO" and editar_correo !="NO" and editar_direccion =="NO":
                contacto_buscado.update({"nombre": editar_nombre,"telefono":editar_telefono,"correo":editar_correo})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break 

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono !="NO" and editar_correo =="NO" and editar_direccion =="NO":
                contacto_buscado.update({"nombre": editar_nombre,"telefono":editar_telefono})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break  
            
            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono =="NO" and editar_correo =="NO" and editar_direccion =="NO":
                contacto_buscado.update({"nombre": editar_nombre})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break 
            
            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono !="NO" and editar_correo !="NO" and editar_direccion !="NO":
                contacto_buscado.update({"telefono":editar_telefono,"correo":editar_correo,"direccion":editar_direccion})
                print(f"Resultado de edición: {contacto_buscado}")  
                encontrado = True
                break
            
            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono !="NO" and editar_correo =="NO" and editar_direccion !="NO":
                contacto_buscado.update({"telefono":editar_telefono,"direccion":editar_direccion}) 
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break
            
            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono !="NO" and editar_correo =="NO" and editar_direccion =="NO":
                contacto_buscado.update({"telefono":editar_telefono}) 
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break
                
            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono !="NO" and editar_correo !="NO" and editar_direccion =="NO":
                contacto_buscado.update({"telefono":editar_telefono,"correo":editar_correo})
                print(f"Resultado de edición: {contacto_buscado}")  
                encontrado = True
                break

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono =="NO" and editar_correo !="NO" and editar_direccion !="NO":
                contacto_buscado.update({"nombre": editar_nombre,"correo":editar_correo,"direccion":editar_direccion})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break 

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono =="NO" and editar_correo !="NO" and editar_direccion =="NO":
                contacto_buscado.update({"nombre": editar_nombre,"correo":editar_correo})
                print(f"Resultado de edición: {contacto_buscado}")  
                encontrado = True
                break

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono =="NO" and editar_correo !="NO" and editar_direccion !="NO":
                contacto_buscado.update({"correo":editar_correo,"direccion":editar_direccion})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break 

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono =="NO" and editar_correo !="NO" and editar_direccion =="NO":
                contacto_buscado.update({"correo":editar_correo})
                print(f"Resultado de edición: {contacto_buscado}")  
                encontrado = True
                break

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono !="NO" and editar_correo =="NO" and editar_direccion !="NO":
                contacto_buscado.update({"nombre": editar_nombre,"telefono":editar_telefono,"direccion":editar_direccion}) 
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break

            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre !="NO" and editar_telefono =="NO" and editar_correo =="NO" and editar_direccion !="NO":
                contacto_buscado.update({"nombre": editar_nombre,"direccion":editar_direccion})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break
            
            elif (contacto_buscado.get("nombre") == dato_buscado or contacto_buscado.get("telefono") == dato_buscado) and editar_nombre =="NO" and editar_telefono =="NO" and editar_correo =="NO" and editar_direccion !="NO":
                contacto_buscado.update({"direccion":editar_direccion})
                print(f"Resultado de edición: {contacto_buscado}") 
                encontrado = True
                break

        if not encontrado:
                 print("No se puede editar el contacto, el contacto no existe o fue mal ingresado el nombre o teléfono.")
            
        #print(self._datos)
        #print(f"Resultado de edición: {contacto_buscado}")
        print("\033[1m_\033[0m"*70) 
        print()

       
    # Médoto para mostrar los contactos existentes
    def ver_contactos(self):
        print(f"{"\033[1mNombre\033[0m":24} {"\033[1mTeléfono\033[0m":25} {"\033[1mCorreo\033[0m":25} {"\033[1mDirección\033[0m"}")
        print("-" * 70)
        for vista in self._datos:
            print(f"{vista["nombre"]:15} {vista["telefono"]:12} {vista["correo"]:25} {vista["direccion"]}")
        print("\033[1m_\033[0m"*70) 
        print()



# Definición del programa para el usuario
def main():
    print("\033[1m*\033[0m"*70)
    print("\n       \033[1mBienvenido al menú del Sistema de gestión de contactos\033[0m\n")
    print("\033[1m*\033[0m"*70)
    print()

    #Opciones del menú
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar contactos")
    print("6. Salir del sistema\n")

    agenda=Contacto()
    opcion = ""
    while opcion != 6:
        opcion= int(input("\033[1mIntroduzca el número de la opción a seleccionar: \033[0m"))

        if opcion == 1:
            print("\n\033[1m1. Agregar contacto\033[0m\n")
            agenda.agregar_contacto()
        
        elif opcion == 2:
            print("\n\033[1m2. Buscar contacto\033[0m\n")
            agenda.buscar_contacto()
        
        elif opcion == 3:
            print("\n\033[1m3. Editar contacto\033[0m\n")
            agenda.editar_contacto()
        
        elif opcion == 4:
            print("\n\033[1m4. Eliminar contacto\033[0m\n")
            agenda.eliminar_contacto()            
        
        elif opcion == 5:
            print("\n\033[1m5. Mostrar contactos\033[0m\n")
            agenda.ver_contactos()
        
        elif opcion == 6:
            print("\n\033[34m\033[1mSaliendo del sistema\033[0m\033[0m\n")
        
        else:
            print("\n\033[33m\033[1mOpción no válida. Por favor, seleccione una opción del menú.\033[0m\033[0m\n")

if __name__== "__main__":
    main()