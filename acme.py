from names import product_names
import random


class Procuct:
    """Class to Load CSV Dataset into a DataFrame"""

    def __init__(self, names=None, price=10, weight=20, flammability=0.1, identifier=1):
        self.names = names
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
        pass
