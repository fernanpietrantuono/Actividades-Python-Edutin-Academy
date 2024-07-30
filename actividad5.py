agenda = {"José": 302944, "Mario": 829455, "Ángel": 829405, "Luis": 930594}

consultando = True

while consultando:
    # El programa arranca abriendo la agenda y su menú de opciones
    print("\nMI AGENDA 📱📠🖥")
    print("--------------------------")
    print("Elegí una opción: \n"
          "1. Consultar \n"
          "2. Agregar \n"
          "3. Modificar \n"
          "4. Eliminar \n"
          "5. Salir \n")
    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

        if opcion == "1":
            # El programa pregunta el nombre
            nombre = input("Nombre: ")
            # Luego lo verifica si aparece en la agenda o no
            if nombre not in agenda:
                print(f'Lo siento, el nombre ingresado ({nombre}) no aparece en la agenda')
            else:
                telefono = agenda[nombre]
                print(f'{nombre} : {telefono}')

        elif opcion == "2":
            # El programa pregunta el nombre
            nombre = input("Nombre: ")
            if nombre in agenda:
                print(f'El nombre ingresado ({nombre}) ya existe en la agenda')
            else:
                # El programa pide el teléfono de la persona registrada y lo agrega
                telefono = int(input("Digitá el teléfono: "))
                agenda = nombre[telefono]
                print("¡Adición exitosa! ✔")

        elif opcion == "3":
            # El programa pregunta el nombre
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print(f'Lo siento, el nombre ingresado ({nombre}) no aparece en la agenda')
            else:
                # El programa pide el teléfono de la persona consultada y lo modifica
                telefono = int(input("Digitá el teléfono: "))
                agenda = nombre[telefono]
                print("¡Modificación exitosa! ✔")

        elif opcion == "4":
            # El programa pregunta el nombre
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print(f'Lo siento, el nombre ingresado ({nombre}) no aparece en la agenda')
            else:
                # El programa elimina la persona de la agenda
                del agenda[nombre]
                print("¡Eliminación exitosa! ✔")

        elif opcion == "5":
            # El programa despide al usuario y abandona el bucle usando un Break
            consultando = False
            print("Muchas gracias por usar el programa, que tengas un buen día 👋🏻.")
            break
        else:
            """ 
            Si el usuario ingresa mal la opción, se mostrará un mensaje de error
            y repetirá el bucle hasta ingresar una de las opciones correctas
            """
            print("\nDisculpame, la opción ingresada es incorrecta. Por favor, intentalo nuevamente.")
