"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        inventory[item] = items.count(item)
    return inventory


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    inventory_list = []
    for key, value in inventory.items():
        if value > 0:
            inventory_list.append((key, value))
    return inventory_list