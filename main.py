import itertools

__author__ = 'swaribrus'

from genetics import generate_class_chromosome
from genetics import shotgun_generator, full_generator, focusing_generator
import random

Chromosome = generate_class_chromosome('binary', 7)
pop = shotgun_generator(Chromosome, 15)
for x in pop.population:
    print(x)