__author__ = 'swaribrus'


class Simulation:
    def __init__(self, population_size=100, chromosome=None, init_population=None, fitness=None):
        self.population_size = population_size
        self.chromosome = chromosome
        self.init_population = init_population
        self.fitness = fitness