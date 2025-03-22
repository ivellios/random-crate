import enum
from dataclasses import dataclass


class ItemTypes(enum.StrEnum):
    wealth = "Wealth"
    gear = "Gear"
    ingredients = "Ingredients"
    meals = "Meals"
    drinks = "Drinks"
    books = "Books"


class ContainerTypes(enum.StrEnum):
    bag = "Bag"
    chest = "Chest"
    pouch = "Pouch"
    crate = "Crate"
    bookshelf = "Bookshelf"
    barrel = "Barrel"
    basket = "Basket"


@dataclass
class Container:
    container_type: ContainerTypes
    contents: dict[ItemTypes, str | int | list[str]]


ADVENTURING_GEAR = [
    "Abacus",
    "Acid (vial)",
    "Alchemist’s fire (flask)",
    "Ammunition: Arrows (20)",
    "Ammunition: Blowgun needles (50)",
    "Ammunition: Crossbow bolts (20)",
    "Ammunition: Sling bullets (20)",
    "Antitoxin (vial)",
    "Arcane focus: Crystal",
    "Arcane focus: Orb",
    "Arcane focus: Rod",
    "Arcane focus: Staff",
    "Arcane focus: Wand",
    "Backpack",
    "Ball bearings (bag of 1,000)",
    "Barrel",
    "Basket",
    "Bedroll",
    "Bell",
    "Blanket",
    "Block and tackle",
    "Book",
    "Bottle, glass",
    "Bucket",
    "Caltrops (bag of 20)",
    "Candle",
    "Case, crossbow bolt",
    "Case, map or scroll",
    "Chain (10 feet)",
    "Chalk (1 piece)",
    "Chest",
    "Climber’s kit",
    "Clothes: Common clothes",
    "Clothes: Costume clothes",
    "Clothes: Fine clothes",
    "Clothes: Traveler’s clothes",
    "Component pouch",
    "Crowbar",
    "Fishing tackle",
    "Flask or tankard",
    "Grappling hook",
    "Hammer",
    "Hammer, sledge",
    "Healer’s kit",
    "Holy symbol: Amulet",
    "Holy symbol: Emblem",
    "Holy symbol: Reliquary",
    "Holy water (flask)",
    "Hourglass",
    "Hunting trap",
    "Ink (1 ounce bottle)",
    "Ink pen",
    "Jug or pitcher",
    "Ladder (10-foot)",
    "Lamp",
    "Lantern: Bullseye lantern",
    "Lantern: Hooded lantern",
    "Lock",
    "Magnifying glass",
    "Manacles",
    "Mess kit",
    "Mirror, steel",
    "Oil (flask)",
    "Paper (one sheet)",
    "Parchment (one sheet)",
    "Perfume (vial)",
    "Pick, miner’s",
    "Piton",
    "Poison, basic (vial)",
    "Pole (10-foot)",
    "Pot, iron",
    "Potion of healing",
    "Pouch",
    "Quiver",
    "Ram, portable",
    "Rations (1 day)",
]


GEMS_BY_VALUE = {
    10: [
        "Azurite",
        "Blue Quartz",
        "Hematite",
        "Lapis Lazuli",
        "Malachite",
        "Obsidian",
        "Rhodochrosite",
        "Tiger Eye",
        "Turquoise",
    ],
    50: [
        "Bloodstone",
        "Carnelian",
        "Chalcedony",
        "Chrysoprase",
        "Citrine",
        "Jasper",
        "Moonstone",
        "Onyx",
        "Quartz",
        "Sardonyx",
        "Star Rose Quartz",
        "Zircon",
    ],
    100: [
        "Amber",
        "Amethyst",
        "Chrysoberyl",
        "Coral",
        "Garnet",
        "Jade",
        "Jet",
        "Pearl",
        "Spinel",
        "Tourmaline",
    ],
    500: [
        "Alexandrite",
        "Aquamarine",
        "Black Pearl",
        "Blue Spinel",
        "Peridot",
        "Topaz",
    ],
    1000: [
        "Black Opal",
        "Blue Sapphire",
        "Emerald",
        "Fire Opal",
        "Opal",
        "Star Ruby",
        "Star Sapphire",
        "Yellow Sapphire",
    ],
    5000: ["Ruby", "Diamond", "Jacinth", "Black Sapphire"],
}


COIN_VALUES_IN_GP = {"cp": 0.01, "sp": 0.1, "ep": 0.5, "gp": 1, "pp": 10}
