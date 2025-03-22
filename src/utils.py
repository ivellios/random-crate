import random

from .consts import ItemTypes, ContainerTypes, Container


def roll_dice(number, sides, chance: int = None):
    if chance:
        if roll_dice(1, 100) > chance:
            return 0
    return sum(random.randint(1, sides) for _ in range(number))


def wealth_to_string(wealth):
    string = ""
    gems = wealth["gems"]
    coins = wealth["coins"]

    if gems:
        string += ", ".join(f"{gem} ({value}gp)" for (gem, value) in gems) + "\n"
    string += ", ".join(f"{value}{coin}" for coin, value in coins.items())

    return string


def items_to_string(container: Container):
    items = container.contents
    gear = items.get(ItemTypes.gear)
    books = items.get(ItemTypes.books)
    ingredients = items.get(ItemTypes.ingredients)
    meals = items.get(ItemTypes.meals)
    drinks = items.get(ItemTypes.drinks)
    wealth = items.get(ItemTypes.wealth)

    items_string = f"{str(container.container_type)}\n"

    if gear:
        items_string += f"{', '.join(gear)}\n"
    if books:
        items_string += f"{str(ItemTypes.books)}: {books}\n"
    if ingredients:
        items_string += f"{str(ItemTypes.ingredients)}: {ingredients}\n"
    if meals:
        items_string += f"{str(ItemTypes.meals)}: {meals}\n"
    if drinks:
        items_string += f"{str(ItemTypes.drinks)}: {drinks}\n"
    if wealth:
        items_string += wealth_to_string(wealth) + "\n"

    return items_string + ""


def to_container(
    container: ContainerTypes, contents: dict[ItemTypes, list | str | int]
):
    return Container(container_type=container, contents=contents)
