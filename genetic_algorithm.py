"""
GENETIC ALGORITHM
"""

import random
import copy

from chromosome import create_population
from data import rooms, timeslots
from fitness import fitness

# ==========================================
# PARAMETER
# ==========================================

POPULATION_SIZE = 60
GENERATIONS = 100
CROSSOVER_RATE = 0.85
MUTATION_RATE = 0.20
ELITE_SIZE = 2

# ==========================================
# TOURNAMENT SELECTION
# ==========================================

def selection(population):
    tournament = random.sample(population, 3)
    tournament.sort(key=lambda ind: fitness(ind)[0], reverse=True)
    return copy.deepcopy(tournament[0])

# ==========================================
# CROSSOVER
# ==========================================

def crossover(parent1, parent2):

    if random.random() > CROSSOVER_RATE:
        return copy.deepcopy(parent1), copy.deepcopy(parent2)

    point = random.randint(1, len(parent1) - 2)

    child1 = copy.deepcopy(parent1[:point] + parent2[point:])
    child2 = copy.deepcopy(parent2[:point] + parent1[point:])

    return child1, child2

# ==========================================
# MUTATION
# ==========================================

def mutation(individual):

    for gene in individual:

        if random.random() < MUTATION_RATE:

            if random.random() < 0.5:
                gene["room"] = random.choice(rooms)
            else:
                gene["timeslot"] = random.choice(timeslots)

    return individual

# ==========================================
# GENETIC ALGORITHM
# ==========================================

def run_genetic_algorithm():

    population = create_population(POPULATION_SIZE)

    best_history = []
    avg_history = []

    best_individual = None

    for generation in range(GENERATIONS):

        population.sort(
            key=lambda ind: fitness(ind)[0],
            reverse=True
        )

        best_individual = copy.deepcopy(population[0])

        max_fit = fitness(best_individual)[0]

        avg_fit = sum(
            fitness(ind)[0]
            for ind in population
        ) / POPULATION_SIZE

        best_history.append(max_fit)
        avg_history.append(avg_fit)

        print(
            f"Generasi {generation+1:3} | "
            f"Max = {max_fit:.2f} | "
            f"Avg = {avg_fit:.2f}"
        )

        # Jika sudah tidak ada konflik, hentikan lebih awal
        if max_fit == 100:
            print("\nSolusi optimal ditemukan!")
            break

        # Elitism
        new_population = [
            copy.deepcopy(ind)
            for ind in population[:ELITE_SIZE]
        ]

        while len(new_population) < POPULATION_SIZE:

            parent1 = selection(population)
            parent2 = selection(population)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    return best_individual, best_history, avg_history