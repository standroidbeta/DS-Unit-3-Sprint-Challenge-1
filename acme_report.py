#!/usr/bin/env python

from random import sample, randint, uniform
from typing import List, Any, Union

from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_product=30):
    """Randomly generates product list"""
    products = [' '.join(sample(ADJECTIVES, 1) + sample(NOUNS, 1))
                for _ in range(num_product)]
    products_set = set(products)
    products = len(products_set)

    return print('Unique number of products:', products)


def inventory_report(products):

    pass


if __name__ == '__main__':
    inventory_report(generate_products())

