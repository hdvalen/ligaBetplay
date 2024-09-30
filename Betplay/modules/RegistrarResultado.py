
import modules.RegistrarEquipos as re
import modules.ProgramarPartido as pp

def registrarResultado(fecha, equipoLocal, golesLocal, equipoVisitante, golesVisitante,AmarillasLocal,RojasLocal,FaltasLocal,AmarillasVisitante,RojasVisitante,FaltasVisitante):
   #Buscar el partido programado en la lista de partidos
   
    partidoEncontrado = next((partido for partido in pp.partidosProgramados if partido["Fecha"] == fecha and partido["Equipo Local"] == equipoLocal and partido["Equipo Visitante"] == equipoVisitante), None)
    
    if partidoEncontrado:
        re.equipos[equipoLocal]["Partidos Jugados"] += 1
        re.equipos[equipoVisitante]["Partidos Jugados"] += 1

        if golesLocal > golesVisitante:
            re.equipos[equipoLocal]["Partidos Ganados"] += 1
            re.equipos[equipoVisitante]["Partidos Perdidos"] += 1
            re.equipos[equipoLocal]["Puntos"] += 3
            print(f"{equipoLocal} ganó el partido contra {equipoVisitante}.")
        
        elif golesLocal < golesVisitante:
            re.equipos[equipoVisitante]["Partidos Ganados"] += 1
            re.equipos[equipoLocal]["Partidos Perdidos"] += 1
            re.equipos[equipoVisitante]["Puntos"] += 3
            print(f"{equipoVisitante} ganó el partido contra {equipoLocal}.")
        
        else:
            re.equipos[equipoLocal]["Partidos Empatados"] += 1
            re.equipos[equipoVisitante]["Partidos Empatados"] += 1
            re.equipos[equipoLocal]["Puntos"] += 1
            re.equipos[equipoVisitante]["Puntos"] += 1
            print(f"El partido entre {equipoLocal} y {equipoVisitante} terminó en empate.")
        
        re.equipos [equipoLocal]["Tarjetas Amarillas"] += AmarillasLocal
        re.equipos [equipoLocal]["Tarjetas Rojas"] += RojasLocal
        re.equipos [equipoLocal]["Faltas"] += FaltasLocal

        re.equipos [equipoVisitante]["Tarjetas Amarillas"] += AmarillasVisitante
        re.equipos [equipoVisitante]["Tarjetas Rojas"] += RojasVisitante
        re.equipos [equipoVisitante]["Faltas"] += FaltasVisitante
    else:
        print("El partido no está programado.")