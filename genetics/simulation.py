__author__ = 'swaribrus'

import random

from .population import Population
from .cross import combine_element_pairs
from .mutate import simple_single_point_mutation


class Simulation:
    pop = None


    def update_fitnes_pop(self):
        for item in self.pop.population:
            item.score = self.fitness(item)


    def __init__(self, population_size=100, chromosome=None,
                 init_population=None, selection_function=None,
                 cross_function = None, fitness=None, mutation_pсt=0.05, elite_size=2, cross_pct=0.7):
        self.population_size = population_size
        self.chromosome = chromosome
        self.init_population = init_population
        self.selection_function = selection_function
        self.cross_function = cross_function
        self.fitness = fitness
        self.mutation_pсt = mutation_pсt
        self.elite_size = elite_size
        self.cross_pct = cross_pct

        self.parents_per_selection = population_size - elite_size

        self.pop = self.init_population(self.chromosome, self.population_size)
        self.update_fitnes_pop()


    def parents(self, scored_population):
        '''
        Given a scored population, use the selection function to find parents
        '''
        return self.selection_function(
            scored_population,
            self.parents_per_selection)


    def pairwise(self, iterable):
        '''
        Given an iterable, yield the items in it in pairs. For instance:

            list(pairwise([1,2,3,4])) == [(1,2), (3,4)]
        '''
        x = iter(iterable)
        return zip(x, x)


    def combine(self, parent1, parent2, combine_mask):
        child1, child2 = combine_element_pairs((c1, c2) if mask else (c2, c1)
                                               for c1, c2, mask in zip(parent1.genes, parent2.genes, combine_mask))

        return self.chromosome(child1), self.chromosome(child2)


    def step_generator(self):
        scored_population = sorted(self.pop.population, reverse=True,
            key=lambda member: member.score)

        yield from scored_population[:self.elite_size]

        for parent1, parent2 in self.pairwise(self.parents(scored_population)):

            mask = [x for x in self.cross_function(self.chromosome.length)]
            for child in self.combine(parent1, parent2, mask):
                if random.randint(0, 100) < self.mutation_pсt:
                    yield self.chromosome(simple_single_point_mutation(child))

    def step(self):
        self.pop = Population(list(self.step_generator()))
        return self.pop


