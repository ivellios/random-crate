from src.containers import generate_loot_containers
from src.utils import items_to_string


def main():
    containers = generate_loot_containers("loots/cr6_loot.yml")
    for container in containers:
        item_string = items_to_string(container)
        sheet_string = f'"{item_string}"'
        print(sheet_string)


if __name__ == "__main__":
    main()
