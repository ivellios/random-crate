import yaml

from . import items
from .consts import ItemTypes, ContainerTypes
from .random_wealth import convert_coins_to_wealth
from .utils import to_container


def make_container(cr, container_type: ContainerTypes):
    with open("configs/containers.yml", "r") as f:
        containers_data = yaml.safe_load(f)

    contents_data = containers_data[container_type.name]
    contents = {}

    if "gear" in contents_data:
        gear = contents_data.pop("gear") or {}
        contents[ItemTypes.gear] = items.random_adventuring_gear(
            **{k: v for k, v in gear.items()}
        )

    if "wealth" in contents_data:
        max_gem_value_percentage = contents_data.pop("wealth", 50)
        contents[ItemTypes.wealth] = convert_coins_to_wealth(
            items.random_individual_treasure(cr), max_gem_value_percentage
        )

    contents.update(
        {
            ItemTypes[k]: getattr(items, f"random_{k}")(v)
            for k, v in contents_data.items()
        }
    )

    container = to_container(container_type, contents)

    return container


def generate_loot_containers(loot_filepath: str):
    with open(loot_filepath, "r") as f:
        loot = yaml.safe_load(f)

    cr = loot.get("cr", 1)
    containers = []
    for container_type, count in loot.get("containers", {}).items():
        for _ in range(count):
            containers.append(make_container(cr, ContainerTypes[container_type]))

    return containers
