import random

from .consts import ADVENTURING_GEAR
from .tables import load_individual_treasure_table
from .utils import roll_dice


def random_adventuring_gear(chance: int = 100, max_count: int = 3):
    amount = roll_dice(1, max_count, chance=chance)
    return [random.choice(ADVENTURING_GEAR) for _ in range(amount)]


def random_individual_treasure(cr: int):
    d100 = random.randint(1, 100)
    return load_individual_treasure_table()[cr][d100].roll()


def random_books(chance: int = 100):
    return roll_dice(1, sides=3, chance=chance)


def random_ingredients(chance: int = 100):
    return roll_dice(1, sides=4, chance=chance)


def random_meals(chance: int = 100):
    return roll_dice(1, sides=1, chance=chance)


def random_drinks(chance: int = 100):
    return roll_dice(1, sides=3, chance=chance)
