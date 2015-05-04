__author__ = 'swaribrus'

import random
import itertools
from .population import Population
from .helper import num2base


def full_generator(Chromosome):

    """
    Function for generate full population
    :param Chromosome: Class chromosome
    :return: Object population
    """

    alphabet = [x for x in range(Chromosome.left_range, Chromosome.right_range + 1)]
    pop = Population()
    pop.population = [
        Chromosome(list(x)) for x in itertools.product(alphabet, repeat=Chromosome.length)
    ]
    return pop


def random_generator(Chromosome, population_size):

    """
    Function for generate init population random
    :param Chromosome: Class chromosome
    :param population_size: population size
    :return: Object population
    """

    pop = Population()
    pop.population = [
        Chromosome([random.randint(Chromosome.left_range, Chromosome.right_range) for _ in range(Chromosome.length)])
        for i in range(population_size)]
    return pop


def shotgun_generator(Chromosome, percent):
    len_full_pop = pow((Chromosome.right_range - Chromosome.left_range)+1, Chromosome.length)
    len_pop = round(len_full_pop*(percent/100))
    alphabet = [x for x in range(Chromosome.left_range, Chromosome.right_range + 1)]
    pop = Population()
    for _ in range(len_pop):
        pop.population.append(Chromosome(num2base(random.randint(0, len_full_pop-1), Chromosome.length, alphabet)))
    return pop


def focusing_generator(Chromosome, center_percent, radius_percent, percent):
    len_full_pop = pow((Chromosome.right_range - Chromosome.left_range)+1, Chromosome.length)
    center = round(len_full_pop*(center_percent/100))
    radius = round(len_full_pop*(radius_percent/100))
    left = center - radius
    right = center + radius
    length = right - left
    len_pop = round(length*(percent/100))
    alphabet = [x for x in range(Chromosome.left_range, Chromosome.right_range + 1)]
    pop = Population()
    for _ in range(len_pop):
        pop.population.append(Chromosome(num2base(random.randint(left, right), Chromosome.length, alphabet)))
    return pop