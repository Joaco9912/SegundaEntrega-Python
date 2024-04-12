def generar_nueva(nombres,goles,goles_evitados,asistencias):
    claves = list(nombres.strip() for nombres in nombres.split(','))
    valores = list(zip(goles,goles_evitados,asistencias))
    return dict(zip(claves,valores))


def goleador(estructura):
    lista_goles_jugador = [tuple([nombre,estadistica[0]]) for nombre,estadistica in estructura.items()]
    return max(lista_goles_jugador,key=lambda x: x[1])


def jugador_mas_influyente(estructura):
    lista_max = [tuple([nombre,sum([estadistica[0]*1.5, estadistica[1]*1.25, estadistica[2]])]) for nombre,estadistica in estructura.items()]
    return max(lista_max,key=lambda x: x[1])


def calcular_promedio_equipo(estructura,total_partidos):
    return sum(goles[0] for goles in estructura.values())/total_partidos

    
def calcular_promedio_jugador(goleador,total_partidos):
    return goleador[1]/total_partidos