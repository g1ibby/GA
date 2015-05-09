import itertools

__author__ = 'swaribrus'

from genetics import generate_class_chromosome
from genetics import shotgun_generator, full_generator, focusing_generator
from genetics import one_point_crossover, two_point_crossover, \
    uniform_point_crossover, combine_element_pairs, three_point_crossover, ordered_one_point_crossover
import random


chromosome = generate_class_chromosome('binary', 15)


def combine(parent1, parent2, combine_mask):
    child1, child2 = combine_element_pairs((c1, c2) if mask else (c2, c1)
                                           for c1, c2, mask in zip(parent1.genes, parent2.genes, combine_mask))

    return chromosome(child1), chromosome(child2)


pop = shotgun_generator(chromosome, 0.01)
print('----- Одноточечный оператор кроссинговера -----')
print(pop.population[0])
print(pop.population[2])

print('-----')
mask_global = [x for x in one_point_crossover(15)]
print(' '.join('1' if x else '0' for x in mask_global))
print('-----')
childrens = combine(pop.population[0], pop.population[2], mask_global)
for ch in childrens:
    print(ch)
print('-----')

print('----- Двухточечный оператор кроссинговера -----')
print(pop.population[0])
print(pop.population[2])

print('-----')
mask_global = [x for x in two_point_crossover(15)]
print(' '.join('1' if x else '0' for x in mask_global))
print('-----')
childrens = combine(pop.population[0], pop.population[2], mask_global)
for ch in childrens:
    print(ch)
print('-----')

print('----- Трехточечный оператор кроссинговера -----')
print(pop.population[0])
print(pop.population[2])

print('-----')
mask_global = [x for x in three_point_crossover(15)]
print(' '.join('1' if x else '0' for x in mask_global))
print('-----')
childrens = combine(pop.population[0], pop.population[2], mask_global)
for ch in childrens:
    print(ch)
print('-----')

print('----- Универсальный оператор кроссинговера -----')
print(pop.population[0])
print(pop.population[2])

print('-----')
mask_global = [x for x in uniform_point_crossover(15)]
print(' '.join('1' if x else '0' for x in mask_global))
print('-----')
childrens = combine(pop.population[0], pop.population[2], mask_global)
for ch in childrens:
    print(ch)
print('-----')

print('----- Одноточечный упорядоченный оператор кроссинговера -----')
chromosomeABC = generate_class_chromosome('char', 15)
popABC = focusing_generator(chromosomeABC, 50, 0.0000000001, 0.000000000001)
# print(popABC.population[0])
# print(popABC.population[2])

print('-----')
# genes1, genes2 = ordered_one_point_crossover(popABC.population[0].genes, popABC.population[2].genes)
genes1, genes2 = ordered_one_point_crossover(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                                             ['G', 'A', 'B', 'E', 'C', 'D', 'F', 'H'])
ch1 = chromosomeABC(genes1)
ch2 = chromosomeABC(genes2)
print(ch1.genes)
print(ch2.genes)
print('-----')