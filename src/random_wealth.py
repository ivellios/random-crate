import random

from .consts import COIN_VALUES_IN_GP, GEMS_BY_VALUE
from .utils import roll_dice


def drg(number: int, multiplier: int = 1, sides: int = 6):
    """AKA Dice Roll Generator"""

    def roll_function():
        return roll_dice(number, sides) * multiplier

    return roll_function


class TreasureRoller:
    def __init__(
        self,
        cp: callable = None,
        sp: callable = None,
        ep: callable = None,
        gp: callable = None,
        pp: callable = None,
    ):
        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp

    def roll(self):
        return {
            coin_type: getattr(self, coin_type)()
            for coin_type in ["cp", "sp", "ep", "gp", "pp"]
            if getattr(self, coin_type)
        }


def treasure_to_gp(treasure: dict):
    return sum(COIN_VALUES_IN_GP[k] * v for k, v in treasure.items())


def gold_to_treasure(
    amount: int, target_coinage: list[str] = ("pp", "gp", "ep", "sp", "cp")
):
    remaining_coins = {}
    sorted_coinage = sorted(
        list(target_coinage), key=lambda c: COIN_VALUES_IN_GP[c], reverse=True
    )

    # Convert leftover_value back into coin denominations
    if "pp" in sorted_coinage and amount >= 100:
        pp_amount = int(amount // 100)
        remaining_coins["pp"] = pp_amount
        amount -= pp_amount * 100

    sorted_coinage.remove("pp")

    for coin in sorted_coinage:
        coin_gp = COIN_VALUES_IN_GP[coin]
        amount = int(amount // coin_gp)
        if amount > 0:
            remaining_coins[coin] = amount
            amount -= amount * coin_gp

    return remaining_coins


def convert_coins_to_wealth(
    coin_dict, max_gem_value_percentage: int | None = 50
) -> dict:
    # Convert all coins to gp
    total_gp = treasure_to_gp(coin_dict)
    max_gem_value = total_gp * (
        max_gem_value_percentage / 100
    )  # At most half can be turned into gems

    gems = []
    remaining_value = max_gem_value

    # Try to add gems starting from the most expensive
    for gem_value in sorted(GEMS_BY_VALUE.keys(), reverse=True):
        while remaining_value >= gem_value:
            gem_name = random.choice(GEMS_BY_VALUE[gem_value])
            gems.append((gem_name, gem_value))
            remaining_value -= gem_value

    # Calculate leftover value (convert to coins again)
    leftover_value = total_gp - max_gem_value + remaining_value
    remaining_coins = gold_to_treasure(leftover_value, ["pp", "gp", "sp", "cp"])

    return {"coins": dict(remaining_coins), "gems": gems}
