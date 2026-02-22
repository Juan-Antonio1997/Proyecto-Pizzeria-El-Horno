#Autor: Juan Antonio Gómez Martín
import acceso_admin as adm
intentos = 3
acceso = 0
config = adm.leer_config()
if len(config) > 0:
    while intentos > 0 and acceso == 0:
        contra = input("Introduce la contraseña de acceso: ")
        if adm.check_password(contra):
            acceso = 1
            adm.acceso_autorizado()
        else:
            intentos -= 1
            if intentos > 1:
                print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
            elif intentos == 1:
                print(f"Contraseña incorrecta. Le queda {intentos} intento.")
            else:
                print(f"Contraseña incorrecta. No le quedan más intentos.")
                adm.acceso_denegado()
else:
    print("Error: El fichero de configuración no existe o no fue encontrado")
if acceso == 1:
    datos = adm.leer_datos()
    if datos != "FileNotFound":
        print(f"Total recaudado: {adm.total_recaudado(datos)}€")
        print(f"Media de gasto por ticket: {adm.media_gasto(datos)}€")
    else:
        print("No se ha encontrado ningún fichero de tickets")