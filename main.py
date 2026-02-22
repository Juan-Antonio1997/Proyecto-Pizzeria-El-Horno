#Autor: Juan Antonio Gómez Martín
from librerias import pedido as ped
try:
    menu = ped.leer_menu()
    ped.imprimir_menu(menu)
    ped.line_skip()
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
                ped.line_skip()
                print("Pedido actual:")
                print("--------------")
                print(pedido)
                ped.line_skip()
            case -1:
                ped.line_skip()
                print("Pedido realizado con éxito. Aquí tiene su ticket: ")
                ped.line_skip()
                print(ped.guardar_pedido(pedido))
            case _:
                print("Por favor, introduzca el ID de un producto del menú (o -1 para finalizar su pedido)")
except FileNotFoundError:
    ped.error_leer_menu()