import yaml

from .random_wealth import TreasureRoller, drg
from .range_dict import RangeDict


def dice_string_to_drg(dice: str):
    """
    Converts a dice string to the drg function
    Examples:
         1d6 -> drg(1)
         2d6x100 -> drg(2, 100)
         3d4x1000 -> drg(3, 1000, 4)
    """
    if "d" not in str(dice):
        return drg(int(dice))

    amount, rest = dice.split("d")

    if "x" in rest:
        die, multiplier = rest.split("x")
        return drg(int(amount), int(multiplier), int(die))

    return drg(int(amount), sides=int(rest))


def load_individual_treasure_table():
    with open("configs/individual_treasure.yml", "r") as f:
        try:
            treasure_data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print("YAML Loading Error: ", exc)

    individual_treasure = RangeDict()
    for cr_range in treasure_data:
        cr = tuple(int(cr_part) for cr_part in cr_range["cr"].split("-"))
        treasure_range = RangeDict()
        for range in cr_range.get("ranges", []):
            roll = tuple(int(roll_part) for roll_part in range.pop("roll").split("-"))
            treasure_range[roll] = TreasureRoller(
                **{
                    coin_type: dice_string_to_drg(dice)
                    for coin_type, dice in range.items()
                }
            )
        individual_treasure[cr] = treasure_range

    return individual_treasure
