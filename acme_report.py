#!/usr/bin/env python

import random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    import random
    products = []
    for n in range(6):
        ' '.join([NOUNS[random.randint(0, len(NOUNS))] for products in range(1)])
    return products


# def inventory_report(products):
#     pass  # TODO - your code! Loop over the products to calculate the report.
#
#
# if __name__ == '__main__':
#     inventory_report(generate_products())
#
