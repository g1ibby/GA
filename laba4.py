__author__ = 'swaribrus'

from genetics import Simulation
from genetics import generate_class_chromosome
from genetics import random_generator
from genetics import tournament
from genetics import two_point_crossover


def fitnes_function(ch):
    return ch.genes[0] + 2 * ch.genes[1] + 3 * ch.genes[2] + 4 * ch.genes[3]


chromosome = generate_class_chromosome('number', 5, 1, 30)

module = Simulation(
    population_size=5,
    chromosome=chromosome,
    init_population=random_generator,
    selection_function=tournament(2),
    cross_function=two_point_crossover,
    fitness=fitnes_function,
    mutation_pсt=40,
    elite_size=2,
    cross_pct=0.7
)

for item in module.pop.population:
    print(item)

module.step()

for item in module.pop.population:
    print(item)