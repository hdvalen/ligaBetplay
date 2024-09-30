
import modules.RegistrarEquipos as re
partidosProgramados = []

def programarPartido(fecha, equipoLocal, equipoVisitante):  
    global partidosProgramados
    if equipoLocal in re.equipos and equipoVisitante in re.equipos:       
        #diccionario con los detalles del partido
        partido = {
            "Fecha": fecha, 
            "Equipo Local": equipoLocal, 
            "Equipo Visitante": equipoVisitante 
        }       
        # Agrega el partido a la lista global 
        partidosProgramados.append(partido)
        print(f"Partido programado entre '{equipoLocal}' y '{equipoVisitante}' para la fecha {fecha}.")   
    else:
        print("Uno o ambos equipos no están registrados. Asegurese de registrarlos primero.")