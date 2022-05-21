# WEEK 8 DAY 4 DAILY CHALLENGE
"""This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
A Gene is a single value 0 or 1, it can mutate (flip).
A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.
Implement these classes as you see fit.
Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.
Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
Write your results in you personal biology research notebook and tell us your conclusion :)."""
import random

# I inverse my intuitive idea (an organism is the most general class and a gene is sub-sib-sub-child to inheritate from the flip method

class Gene:
    def __init__(self, value):
        self.value = value
        self.muted = False

    def flip(self):
        random_num = random.randint(0, 1)  # assumption : proba that a gene mutes is 1/2 (strange! I would have said 1/1000 in average).
        if random_num == 0:   # 1 could have been chosen, it is not the value of the gene
            self.value = 0 if self.value else 1
            self.muted = True
        return self.value


class Chromosome(Gene):
    def flip(self):
        for i in range(len(self.value)):
            gene = Gene(self.value[i])
            flipped_gene = gene.flip()
            self.value[i] = flipped_gene
        #print(self.value)
        return self.value


class DNA(Chromosome):
    def flip(self):
        for i in range(len(self.value)):
            chromo = Chromosome(self.value[i])
            flipped_chromo = chromo.flip()
            self.value[i] = flipped_chromo
        print(self.value)
        return self.value

# class Organism(DNA): all the probability topics are not clear, especially here (how can we force the probability of an organism if it was random for genes)
# a gene can mute and remute ?


# TESTING


g = Gene(0)
flipped_g = g.flip()
print(flipped_g)

ch = Chromosome([0, 1, 1, 0, 1, 1, 1, 1, 0, 1])
ch.flip()


my_dna = DNA([[0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
])
my_dna.flip()


dna1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

counter = 0
while my_dna.value != dna1:
    my_dna.flip()
    counter += 1
    print(counter)
print(f'Number of generations is {counter}')

#Not even tried neither to wait for an end of the loop nor to calculate the probability to have 1 everywhere with such a process



