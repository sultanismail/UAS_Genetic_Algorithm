"""
CHROMOSOME
"""

import random

from data import courses
from data import rooms
from data import timeslots


def create_individual():
    """
    Membuat satu individu (jadwal lengkap)
    """

    individual = []

    for course, lecturer in courses:

        gene = {
            "course": course,
            "lecturer": lecturer,
            "room": random.choice(rooms),
            "timeslot": random.choice(timeslots)
        }

        individual.append(gene)

    return individual


def create_population(population_size):
    """
    Membuat populasi awal
    """

    return [
        create_individual()
        for _ in range(population_size)
    ]