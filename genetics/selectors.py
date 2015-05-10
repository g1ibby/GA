__author__ = 'swaribrus'

import random
import bisect
import itertools


def tournament(tournament_size):
    def tournament_selector(population, num_parents):
        for _ in range(num_parents):
            yield max(random.sample(population, tournament_size), key=lambda member: member.score())
    return tournament_selector


def roulette(population, num_parents):
    #Uses code taken from
    #http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice

    cumulative_scores = list(
        itertools.accumulate(member.score for member in population))
    total = cumulative_scores[-1]

    for _ in range(num_parents):
        yield population[
            bisect.bisect(cumulative_scores, random.uniform(0, total))]


