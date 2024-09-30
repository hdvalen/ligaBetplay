
import modules.RegistrarEquipos as re

def mostrarResultados():
    #si hay equipos regis en el diccionario 
    if re.equipos:
        print("\nEstadísticas de los equipos:")
         # repetir sobre cada equipo y sus estadísticas
        for equipo, estadisticas in re.equipos.items():
            print(f"\nEquipo: {equipo}")
            print(f"  Partidos Jugados: {estadisticas['Partidos Jugados']}")
            print(f"  Partidos Ganados: {estadisticas['Partidos Ganados']}")
            print(f"  Partidos Empatados: {estadisticas['Partidos Empatados']}")
            print(f"  Partidos Perdidos: {estadisticas['Partidos Perdidos']}")
            print(f"  Puntos: {estadisticas['Puntos']}")
            print(f"  Tarjetas Amarillas: {estadisticas['Tarjetas Amarillas']}")
            print(f"  Tarjetas Rojas: {estadisticas['Tarjetas Rojas']}")
            print(f"  Faltas: {estadisticas['Faltas']}")
            
    else:
        print("No hay equipos registrados aún.")

