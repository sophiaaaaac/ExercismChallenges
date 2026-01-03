"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart.update({item: 1})
    return current_cart


    
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    pass


def read_notes(notes):
    cart_dict = dict.fromkeys(notes, 1)
    return cart_dict
    
    
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    pass


def update_recipes(ideas, recipe_updates):
    ideas |= recipe_updates
    return ideas

    
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    pass


def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart
    
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    pass


def send_to_store(cart, aisle_mapping):
    new_dict = {}
    for item in cart: #loops over the keys
        '''
        new_dict[Banana] = [cart[Banana]] + aisle_mapping[Banana]
        new_dict[Banana] = [3] + [Aisle 3, False]
        new_dict[Banana] = [3, Aisle 3, False]
        dict_name[Key] = value -> automatically adds to dict
        '''
        new_dict[item] = [cart[item]] + aisle_mapping[item]  
    sorted_dict = dict(sorted(new_dict.items(), reverse=True))
    return sorted_dict
        
    
    
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    pass


def update_store_inventory(fulfillment_cart, store_inventory):
    updated_inventory = {}
    #first check the item is in store and subtract amount bought
    for item in store_inventory:
        if item in fulfillment_cart:
            #access nested tuple value using dict[item][index]
            #e.g. cart['Apple'][1] = [10, 'Aisle 1', False][1] = ['Aisle 1']
            new_item_count = store_inventory[item][0] - fulfillment_cart[item][0]
        else:
            new_item_count = store_inventory[item][0]

        #check if items are out of stock
        if new_item_count <= 0:
            store_inventory[item] =  ["Out of Stock", store_inventory[item][1] , store_inventory[item][2]]
        else:
            store_inventory[item] = [new_item_count , store_inventory[item][1] , store_inventory[item][2]]
    return store_inventory
    
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    pass
