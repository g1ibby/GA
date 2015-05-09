__author__ = 'swaribrus'

from genetics import generate_class_chromosome
from genetics import simple_single_point_mutation, simple_two_point_mutation, \
    mutation_inversion, mutation_translocation

chromosome = generate_class_chromosome('binary', 10)



print('----- Простая одноточечная мутация -----')
ch = chromosome([0, 1, 1, 0, 0, 0, 1, 1, 0, 1])
print(ch)
print('-----')
ch_result = chromosome(simple_single_point_mutation(ch, 5))
print(ch_result)
print('-----')

print('----- Простая двухточечная мутация -----')
ch = chromosome([0, 1, 1, 0, 0, 0, 1, 1, 0, 1])
print(ch)
print('-----')
ch_result = chromosome(simple_two_point_mutation(ch, 2, 5))
print(ch_result)
print('-----')

print('----- Мутация инверсии -----')
ch = chromosome([0, 1, 1, 0, 0, 0, 1, 1, 0, 1])
print(ch)
print('-----')
ch_result = chromosome(mutation_inversion(ch, 2, 5))
print(ch_result)
print('-----')

print('----- Мутация транслокации -----')
chromosomeABC = generate_class_chromosome('char', 6)
parent1 = chromosome(['A', 'B', 'C', 'D', 'E', 'F'])
parent2 = chromosome(['G', 'K', 'H', 'I', 'J', 'Q'])
print(parent1.genes)
print(parent2.genes)
print('-----')
ch1, ch2 = mutation_translocation(parent1, parent2, 2)
print(ch1)
print(ch2)
print('-----')