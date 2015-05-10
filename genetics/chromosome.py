__author__ = 'swaribrus'


def generate_class_chromosome(type, len, l=0, r=9):
    if type == 'number':
        class NumberChromosome:

            type = 'number'
            genes = []
            score = 0
            length = len
            left_range = l
            right_range = r

            def __init__(self, genes):
                self.genes = genes

            def __str__(self):
                return ' '.join(str(x) for x in self.genes) + ' | ' + str(self.score)

        return NumberChromosome

    if type == 'binary':
        class BinaryChromosome:

            type = 'binary'
            genes = []
            score = 0
            length = len
            left_range = 0
            right_range = 1

            def __init__(self, genes):
                self.genes = genes

            def __str__(self):
                return ' '.join('1' if x else '0' for x in self.genes)

        return BinaryChromosome

    if type == 'char':
        class CharChromosome:

            type = 'char'
            genes = []
            score = 0
            length = len
            left_range = 32
            right_range = 121

            def __init__(self, genes):
                self.genes = genes

            def __str__(self):
                return ''.join(chr(x) for x in self.genes)

        return CharChromosome
