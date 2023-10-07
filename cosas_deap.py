from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from problema import NOMBRES_OSOS
from problema import COLORES_OSO
from problema import SOBRINAS
from problema import ACCESORIOS_OSO
from problema import TAM_OSO
from problema import CANT_OSO
from problema import funcion_puntaje
from problema import crear_ind
from problema import imprimir_ind
import numpy

#Busca el menor peso
creator.create("FitnessMax", base.Fitness, weights = (1.0,))

#Crea individuo
creator.create("Individual", list, fitness=creator.FitnessMax, strategy = None)

creator.create("Strategy", list, typecode="d")

#Registra
toolbox = base.Toolbox()

IND_SIZE = TAM_OSO * CANT_OSO
#funcion creadora de individuo
toolbox.register("individual", crear_ind, creator.Individual, creator.Strategy)
#funcion creadora de poblacion
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#funcion evaluadora de pesos
toolbox.register("evaluate", funcion_puntaje)
toolbox.register("select", tools.selTournament, tournsize=10)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate",  tools.mutUniformInt, low = 1, up = 4, indpb=0.1)


pop = toolbox.population(n=100)

hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)

stats.register("avg", numpy.mean, axis=0)
stats.register("std", numpy.std, axis=0)
stats.register("min", numpy.min, axis=0)
stats.register("max", numpy.max, axis=0)


# Evolution
ngen = 200
npop = 1000
pop, logbook = algorithms.eaMuPlusLambda(pop, toolbox, mu=npop, lambda_=npop, cxpb=0.7,   mutpb=0.3, ngen=ngen, stats=stats, halloffame=hof)

best_solution = tools.selBest(pop, 1)[0]
print("\nBEST SOLUTION:")
print("")
print(best_solution)

imprimir_ind(best_solution)
