#Autor: Juan Antonio Gómez Martín
from librerias import pedido as ped, acceso_admin as adm, menu_principal as menp
menu_opcion = 0
while menu_opcion not in range(1,4):
    menp.line_skip()
    menp.main_menu()
    menp.line_skip()
    try:
        menu_opcion = int(input("Introduce una de las opciones del menú: "))
    except ValueError:
        menu_opcion = 0
    match menu_opcion:
        case 1:
            intentos = 3
            acceso = 0
            config = adm.leer_config()
            if len(config) > 0:
                while intentos > 0 and acceso == 0:
                    menp.line_skip()
                    contra = input("Introduce la contraseña de acceso: ")
                    if adm.check_password(contra):
                        acceso = 1
                        adm.acceso_autorizado()
                    else:
                        intentos -= 1
                        if intentos > 1:
                            menp.line_skip()
                            print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
                        elif intentos == 1:
                            menp.line_skip()
                            print(f"Contraseña incorrecta. Le queda {intentos} intento.")
                        else:
                            menp.line_skip()
                            print(f"Contraseña incorrecta. No le quedan más intentos.")
                            adm.acceso_denegado()
            else:
                menp.line_skip()
                print("Error: El fichero de configuración no existe o no fue encontrado")
            if acceso == 1:
                menp.line_skip()
                datos = adm.leer_datos()
                if datos != "FileNotFound":
                    print(f"Total recaudado: {adm.total_recaudado(datos)}€")
                    print(f"Media de gasto por ticket: {adm.media_gasto(datos)}€")
                else:
                    print("No se ha encontrado ningún fichero de tickets")
            menp.line_skip()
        case 2:
            menp.line_skip()
            try:
                menu = ped.leer_menu()
                ped.imprimir_menu(menu)
                menp.line_skip()
                pedido = ped.crear_pedido()
                opcion = 0
                while opcion != -1:
                    try:
                        opcion = int(input("Introduce el ID de uno de los productos del menú (o \"-1\" para cerrar su pedido): "))
                    except ValueError:
                        opcion = 0
                    match opcion:
                        case opcion if opcion in range(1, 11):
                            pedido = ped.agregar_al_pedido(menu, pedido, opcion)
                            menp.line_skip()
                            print("Pedido actual:")
                            print("--------------")
                            print(pedido)
                            menp.line_skip()
                        case -1:
                            menp.line_skip()
                            print("Pedido realizado con éxito. Aquí tiene su ticket: ")
                            menp.line_skip()
                            print(ped.guardar_pedido(pedido))
                            menp.line_skip()
                        case _:
                            print("Por favor, introduzca el ID de un producto del menú (o -1 para finalizar su pedido)")
            except FileNotFoundError:
                ped.error_leer_menu()
                menp.line_skip()
        case 3:
            menp.line_skip()
            print("Saliendo del programa...")
            menp.line_skip()
        case _:
            menp.line_skip()
            print("Por favor, introduzca una de las opciones del menú")