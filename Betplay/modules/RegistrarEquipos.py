
equipos = {}

def registrarEquipo(nombre):
    global equipos
    if nombre not in equipos:
        #Se registra en un diccionario  de estadistica
        equipos[nombre] = { 
            "Partidos Jugados": 0,
            "Partidos Ganados": 0,
            "Partidos Empatados": 0,
            "Partidos Perdidos": 0,
            "Puntos": 0,
            "Tarjetas Amarillas": 0,
            "Tarjetas Rojas": 0,
            "Faltas": 0
        }
        print(f"Equipo '{nombre}' registrado exitosamente.")
    else:
        print(f"El equipo '{nombre}' ya está registrado.")