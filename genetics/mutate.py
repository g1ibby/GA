__author__ = 'swaribrus'

import itertools
import random


def simple_single_point_mutation(chromosome, pos=None):
    if not pos:
        pos = random.randint(0, len(chromosome.genes))

    chromosome.genes[pos+1], chromosome.genes[pos] = \
        chromosome.genes[pos], chromosome.genes[pos+1]
    return chromosome.genes


def simple_two_point_mutation(chromosome, pos1=None, pos2=None):
    if not pos1 or not pos2:
        pos1 = random.randint(0, len(chromosome.genes))
        pos2 = random.randint(pos1, len(chromosome.genes))

    chromosome.genes[pos1+1], chromosome.genes[pos2+1] = \
        chromosome.genes[pos2+1], chromosome.genes[pos1+1]
    return chromosome.genes


def mutation_inversion(chromosome, pos1=None, pos2=None):
    if not pos1 or not pos2:
        pos1 = random.randint(0, len(chromosome.genes))
        pos2 = random.randint(pos1, len(chromosome.genes))

    reverse = chromosome.genes[pos1:pos2]
    chromosome.genes[pos1:pos2] = reverse[::-1]
    return chromosome.genes


def mutation_translocation(ch1, ch2, pos):
    if not pos:
        pos = random.randint(0, len(ch1.genes))

    children1 = ch1.genes[:pos]
    children2 = ch2.genes[:pos]

    reverse = ch2.genes[pos:]
    children1 = children1 + reverse[::-1]

    reverse = ch1.genes[pos:]
    children2 = children2 + reverse[::-1]

    return children1, children2