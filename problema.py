import random
from enum import IntEnum

NOMBRES_OSOS = IntEnum("NOMBRE", ["PEPE", "PACO", "TITO", "QUIQUE"])
SOBRINAS = IntEnum("SOBRINA", ["MALENA", "ELEONORA", "INES", "ZOE"])
COLORES_OSO = IntEnum("COLOR" ,["MARRON", "NEGRO", "GRIS", "BLANCO"])
ACCESORIOS_OSO = IntEnum("ACCESORIO", ["CORBATA", "TARRO_DE_MIEL", "SOMBRERO", "ANTEOJOS"])

POS_SOBRINA = 0
POS_COLOR = 1
POS_ACCESORIO = 2

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

def verificar_existe(v, pos_atr1, val1, pos_atr2, val2):
    for i in range(4):
        if(verificar_condicion(v, i, pos_atr1, val1, pos_atr2, val2)):
            return True
    return False

def verificar_oso_condicion(v, index_oso, pos_atr, val):
    return v[(index_oso -1) * TAM_OSO + pos_atr] == val

def cuanto_se_repiten(v):
    puntaje = 0
    for i in range(0,TAM_OSO * CANT_OSO):
        for j in range(i + TAM_OSO, CANT_OSO * TAM_OSO, TAM_OSO):
            if v[i % (CANT_OSO * TAM_OSO)] == v[j % (CANT_OSO * TAM_OSO)]:
                puntaje += 1
            
    return puntaje

def calcular_condiciones_a_cumplir(ind):
    puntos = 0

    #El oso marron tiene corbata
    if verificar_existe(ind, POS_COLOR, COLORES_OSO.MARRON, POS_ACCESORIO, ACCESORIOS_OSO.CORBATA):
        puntos += 2
    #El oso negro tiene un tarro de miel
    if verificar_existe(ind, POS_COLOR, COLORES_OSO.NEGRO, POS_ACCESORIO, ACCESORIOS_OSO.TARRO_DE_MIEL):
        puntos += 2
    #El oso de Eleonora se llama Pepe
    if verificar_oso_condicion(ind, NOMBRES_OSOS.PEPE, POS_SOBRINA, SOBRINAS.ELEONORA):
        puntos += 2
    #Ines tiene al oso Paco
    if verificar_oso_condicion(ind, NOMBRES_OSOS.PACO, POS_SOBRINA, SOBRINAS.INES):
        puntos += 2
    #El oso Tito es gris
    if verificar_oso_condicion(ind, NOMBRES_OSOS.TITO, POS_COLOR, COLORES_OSO.GRIS):
        puntos += 2
    #El oso Quique es blanco
    if verificar_oso_condicion(ind, NOMBRES_OSOS.QUIQUE, POS_COLOR, COLORES_OSO.BLANCO):
        puntos += 2
    #Zoe tiene el oso con anteojos
    if verificar_existe(ind, POS_SOBRINA, SOBRINAS.ZOE, POS_ACCESORIO, ACCESORIOS_OSO.ANTEOJOS):
        puntos += 2

    return puntos

def calcular_restricciones(ind):
    puntos = 0

    puntos -= cuanto_se_repiten(ind) * 2

    #El oso que se queda Malena no es marron
    if verificar_existe(ind, POS_SOBRINA, SOBRINAS.MALENA, POS_COLOR, COLORES_OSO.MARRON):
        puntos -= 2

    #El oso que se queda Malena no tiene corbata
    if verificar_existe(ind, POS_SOBRINA, SOBRINAS.MALENA, POS_ACCESORIO, ACCESORIOS_OSO.CORBATA):
        puntos -= 2
    
    #Eleonora no se queda con el oso negro
    if verificar_existe(ind, POS_SOBRINA, SOBRINAS.ELEONORA, POS_COLOR, COLORES_OSO.NEGRO):
        puntos -= 2

    #Eleonora no se queda con el que tiene un tarro de miel
    if verificar_existe(ind, POS_SOBRINA, SOBRINAS.ELEONORA, POS_ACCESORIO, ACCESORIOS_OSO.TARRO_DE_MIEL):
        puntos -= 2
    
    #El oso llamado Pepe no es el oso negro el que tiene un tarro de miel
    if verificar_oso_condicion(ind, NOMBRES_OSOS.PEPE, POS_COLOR, COLORES_OSO.NEGRO):
        puntos -= 2

    #El oso llamado Pepe no es el que tiene un tarro de miel
    if verificar_oso_condicion(ind, NOMBRES_OSOS.PEPE, POS_ACCESORIO, ACCESORIOS_OSO.TARRO_DE_MIEL):
        puntos -= 2

    
    #El oso que lleva sombrero no es el oso Tito o el de color gris
    if verificar_oso_condicion(ind, NOMBRES_OSOS.TITO, POS_ACCESORIO, ACCESORIOS_OSO.SOMBRERO):
        puntos -= 2

    #El oso que lleva sombrero no es el de color gris
    if verificar_existe(ind, POS_COLOR, COLORES_OSO.GRIS, POS_ACCESORIO, ACCESORIOS_OSO.SOMBRERO):
        puntos -= 2
    
    #Zoe no tiene al oso Quique o al oso blanco
    if verificar_oso_condicion(ind, NOMBRES_OSOS.QUIQUE, POS_SOBRINA, SOBRINAS.ZOE):
        puntos -= 2
    
    #Zoe no tiene al oso blanco
    if verificar_existe(ind, POS_SOBRINA, SOBRINAS.ZOE, POS_COLOR, COLORES_OSO.BLANCO):
        puntos -= 2

    
    #El oso con anteojos no se llama Quique
    if verificar_oso_condicion(ind, NOMBRES_OSOS.QUIQUE, POS_ACCESORIO, ACCESORIOS_OSO.ANTEOJOS):
        puntos -= 2

    #El oso con anteojos no es blanco
    if verificar_existe(ind, POS_COLOR, COLORES_OSO.BLANCO, POS_ACCESORIO, ACCESORIOS_OSO.ANTEOJOS):
        puntos -= 2

    return puntos

def funcion_puntaje(ind):
    puntos = 0
    puntos += calcular_condiciones_a_cumplir(ind)
    puntos += calcular_restricciones(ind)

    return [puntos]