__author__ = 'swaribrus'

import itertools
import random


def one_point_crossover(length):
    point = random.randint(0, length)
    yield from itertools.repeat(True, point)
    yield from itertools.repeat(False, length - point)


def two_point_crossover(length):
    point1, point2 = sorted(random.randint(0, length) for _ in range(2))
    yield from itertools.repeat(True, point1)
    yield from itertools.repeat(False, point2 - point1)
    yield from itertools.repeat(True, length - point2)


def three_point_crossover(length):
    point1, point2, point3 = sorted(random.randint(0, length) for _ in range(3))
    yield from itertools.repeat(True, point1)
    yield from itertools.repeat(False, point2 - point1)
    yield from itertools.repeat(True, point3 - point2)
    yield from itertools.repeat(False, length - point3)


def uniform_point_crossover(length):
    return (random.choice((False, True)) for i in range(length))


def ordered_one_point_crossover(genes1, genes2):
    length = len(genes1)
    point = random.randint(0, length)
    child1 = []
    child1 = genes1[:point]
    for x in genes2:
        if x not in child1:
            child1.append(x)

    child2 = []
    child2 = genes2[point:]
    for x in genes1:
        if x not in child2:
            child2.append(x)

    return child1, child2


def combine_element_pairs(pairs):
    return tuple(zip(*pairs))

