import random
from enum import IntEnum

NOMBRES_OSOS = IntEnum("NOMBRE", ["PEPE", "PACO", "TITO", "QUIQUE"])
SOBRINAS = IntEnum("SOBRINA", ["MALENA", "ELEONORA", "INES", "ZOE"])
COLORES_OSO = IntEnum("COLOR" ,["MARRON", "NEGRO", "GRIS", "BLANCO"])
ACCESORIOS_OSO = IntEnum("ACCESORIO", ["CORBATA", "TARRO_DE_MIEL", "SOMBRERO", "ANTEOJOS"])

POS_SOBRINA = 0
POS_ACCESORIO = 1
POS_COLOR = 2

TAM_OSO = 3
CANT_OSO = 4

def imprimir_ind(ind):
    for i in range(CANT_OSO):
        print("Oso:" + NOMBRES_OSOS(i + 1).name)
        print("\tSobrina: " + SOBRINAS(ind[i * TAM_OSO + POS_SOBRINA]).name)
        print("\tColor: " + COLORES_OSO(ind[i * TAM_OSO + POS_COLOR]).name)
        print("\tAccesorio: " + ACCESORIOS_OSO(ind[i * TAM_OSO + POS_ACCESORIO]).name)

def crear_ind(cls, str_cls):
    ind = cls()
    for i in range(CANT_OSO * TAM_OSO):
        ind.append(random.randint(1, 4))
    
    ind.strategy = str_cls()
    return ind

def verificar_condicion(v, index_oso, pos_atr1, val1, pos_atr2, val2):
    pos_absoluta1 = (index_oso -1) * TAM_OSO + pos_atr1
    pos_absoluta2 = (index_oso -1) * TAM_OSO + pos_atr2
    return v[pos_absoluta1] == val1 and v[pos_absoluta2] == val2  

def verificiar_existe(v, pos_atr1, val1, pos_atr2, val2):
    for i in range(4):
        if(verificar_condicion(v, i, pos_atr1, val1, pos_atr2, val2)):
            return True
    return False

def verificar_oso_condicion(v, index_oso, pos_atr, val):
    return v[(index_oso -1) * TAM_OSO + pos_atr] == val

def no_se_repiten(v):
    for i in range(0,TAM_OSO * CANT_OSO):
        for j in range(i + TAM_OSO, CANT_OSO * TAM_OSO + i, TAM_OSO):
            if v[i % (CANT_OSO * TAM_OSO)] == v[j % (CANT_OSO * TAM_OSO)]:
                return False
            
    return True

def calcular_condiciones_a_cumplir(ind):
    puntos = 0

    #TODO: no se repiten caracteristicas
    if no_se_repiten(ind):
        puntos += 5

    #El oso marron tiene corbata
    if verificiar_existe(ind, POS_COLOR, COLORES_OSO.MARRON, POS_ACCESORIO, ACCESORIOS_OSO.CORBATA):
        puntos += 5
    #El oso negro tiene un tarro de miel
    if verificiar_existe(ind, POS_COLOR, COLORES_OSO.NEGRO, POS_ACCESORIO, ACCESORIOS_OSO.TARRO_DE_MIEL):
        puntos += 5
    #El oso de Eleonora se llama Pepe
    if verificar_oso_condicion(ind, NOMBRES_OSOS.PEPE, POS_SOBRINA, SOBRINAS.ELEONORA):
        puntos += 5
    #Ines tiene al oso Paco
    if verificar_oso_condicion(ind, NOMBRES_OSOS.PACO, POS_SOBRINA, SOBRINAS.INES):
        puntos += 5
    #El oso Tito es gris
    if verificar_oso_condicion(ind, NOMBRES_OSOS.TITO, POS_COLOR, COLORES_OSO.GRIS):
        puntos += 5
    #El oso Quique es blanco
    if verificar_oso_condicion(ind, NOMBRES_OSOS.QUIQUE, POS_COLOR, COLORES_OSO.BLANCO):
        puntos += 5
    #Zoe tiene el oso con anteojos
    if verificiar_existe(ind, POS_SOBRINA, SOBRINAS.ZOE, POS_ACCESORIO, ACCESORIOS_OSO.ANTEOJOS):
        puntos += 5

    return puntos

def calcular_restricciones(ind):
    puntos = 0

    #El oso que se queda Malena es marron, o tiene corbata
    if not (verificiar_existe(ind, POS_SOBRINA, SOBRINAS.MALENA, POS_COLOR, COLORES_OSO.MARRON) ^ verificiar_existe(ind, POS_SOBRINA, SOBRINAS.MALENA, POS_ACCESORIO, ACCESORIOS_OSO.CORBATA)):
        puntos -= 3
    #Eleonora se queda con el oso negro, o con el que tiene un tarro de miel
    if not (verificiar_existe(ind, POS_SOBRINA, SOBRINAS.ELEONORA, POS_COLOR, COLORES_OSO.NEGRO) ^ verificiar_existe(ind, POS_SOBRINA, SOBRINAS.ELEONORA, POS_ACCESORIO, ACCESORIOS_OSO.TARRO_DE_MIEL)):
        puntos -= 3
    #El oso llamado Pepe es el oso negro, o el que tiene un tarro de miel
    if not (verificar_oso_condicion(ind, NOMBRES_OSOS.PEPE, POS_COLOR, COLORES_OSO.NEGRO) ^ verificar_oso_condicion(ind, NOMBRES_OSOS.PEPE, POS_ACCESORIO, ACCESORIOS_OSO.TARRO_DE_MIEL)):
        puntos -= 3
    #El oso que lleva sombrero es el oso Tito o el de color gris
    if not (verificar_oso_condicion(ind, NOMBRES_OSOS.TITO, POS_ACCESORIO, ACCESORIOS_OSO.SOMBRERO) ^ verificiar_existe(ind, POS_COLOR, COLORES_OSO.GRIS, POS_ACCESORIO, ACCESORIOS_OSO.SOMBRERO)):
        puntos -= 3
    #Zoe tiene al oso Quique o al oso blanco
    if not (verificar_oso_condicion(ind, NOMBRES_OSOS.QUIQUE, POS_SOBRINA, SOBRINAS.ZOE) ^ verificiar_existe(ind, POS_SOBRINA, SOBRINAS.ZOE, POS_COLOR, COLORES_OSO.BLANCO)):
        puntos -= 3
    #El oso con anteojos se llama Quique o es blanco
    if not (verificar_oso_condicion(ind, NOMBRES_OSOS.QUIQUE, POS_ACCESORIO, ACCESORIOS_OSO.ANTEOJOS) ^ verificiar_existe(ind, POS_COLOR, COLORES_OSO.BLANCO, POS_ACCESORIO, ACCESORIOS_OSO.ANTEOJOS)):
        puntos -= 3

    return puntos

def funcion_puntaje(ind):
    puntos = 0
    puntos += calcular_condiciones_a_cumplir(ind)
    puntos += calcular_restricciones(ind)

    return [puntos]