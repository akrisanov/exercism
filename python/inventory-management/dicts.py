from collections import Counter


def create_inventory(items: list) -> dict:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in items}


def add_items(inventory: dict, items: list) -> dict:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    item_counts = create_inventory(items)
    return dict(Counter(inventory) + Counter(item_counts))


def decrement_items(inventory: dict, items: list) -> dict:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: dict) -> list[tuple]:
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [item_tuple for item_tuple in inventory.items() if item_tuple[1] > 0]
