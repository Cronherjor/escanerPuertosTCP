import socket

def escanearPuertos(ip, rangoPuerto):
    # LISTAS EN LAS CUALES VAN A GUARDARSE LOS PÚERTOS ABIERTOS Y CERRADOS
    puertosAbiertos = []
    puertosCerrados = []

    # Recorrer los puertos
    for puerto in range(rangoPuerto[0], rangoPuerto[1] + 1):
        # Crear el socket 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Añadir un tiempo de espera para la conexión
        s.settimeout(2)

        # Intentar la conexión al puerto
        resultado = s.connect_ex((ip, puerto))
        # Si el puerto está abierto el resultado será 0
        if resultado == 0:
            puertosAbiertos.append(puerto)
        else:
            puertosCerrados.append(puerto)
        s.close()
    
    # Retorna los puertos
    return puertosAbiertos, puertosCerrados

# Solicitar al usuario la dirección IP y el rango de puertos
ip = input("Ingrese la dirección IP a escanear: ")
puerto_inicio = int(input("Ingrese el puerto inicial del rango: "))
puerto_fin = int(input("Ingrese el puerto final del rango: "))

# Escanear los puertos
abiertos, cerrados = escanearPuertos(ip, (puerto_inicio, puerto_fin))

print(f'Puertos abiertos: {abiertos}')
print(f'Puertos cerrados: {cerrados}')
