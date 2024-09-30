
import modules.RegistrarEquipos as re
import modules.ProgramarPartido as pp
import modules.RegistrarResultado as rr
import modules.MostrarResultados as mr



if __name__ == "__main__":
    while True:
        print("\n--- Liga BetPlay ---")
        print("1. Registrar equipo")
        print("2. Programar partido")
        print("3. Registrar resultado de partido")
        print("4. Mostrar resultados")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            equipo = input("Nombre del equipo: ")
            re.registrarEquipo(equipo)

        elif opcion == "2":
            fecha = input("Fecha del partido (dia, mes, año): ")
            equipoLocal = input("Equipo local: ")
            equipoVisitante = input("Equipo visitante: ")
            pp.programarPartido(fecha, equipoLocal, equipoVisitante)

        elif opcion == "3":
            fecha = input("Fecha del partido (dia, mes, año): ")
            equipoLocal = input("Equipo local: ")
            golesLocal = int(input(f"Goles de {equipoLocal}: "))
            AmarillaLocal=int(input(f'Tarjetas amarillas del equipo {equipoLocal}:'))
            RojaLocal=int(input(f'Tarjetas rojas del equipo {equipoLocal}:'))
            FaltasLocal= int(input(f"Faltas del equipo {equipoLocal} :"))
            equipoVisitante = input("Equipo visitante: ")
            golesVisitante = int(input(f"Goles de {equipoVisitante}: "))
            AmarillaVisitante=int(input(f'Tarjetas amarillas del equipo {equipoVisitante}:'))
            RojaVisitante=int(input(f'Tarjetas rojas del equipo {equipoVisitante}:'))
            FaltasVisitante=int(input(f"Faltas del equipo {equipoVisitante}:"))

            rr.registrarResultado(fecha, equipoLocal, golesLocal, equipoVisitante, golesVisitante,AmarillaLocal, RojaLocal, FaltasLocal,AmarillaVisitante, RojaVisitante, FaltasVisitante)

        elif opcion == "4":
            mr.mostrarResultados()

        elif opcion == "5":
            print("Saliendo")
            break

        else:
            print("Opción no válida. Intente de nuevo.")



