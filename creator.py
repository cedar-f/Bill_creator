import pandas as pd
from mongo_communicator import Communnicator
import random


class Creator:
    name_list = []
    product_list = []
    bill_store_name = ''

    def __init__(self):
        mongo = Communnicator('product_thegioididong')
        self.name_list = mongo.get_list_name()
        self.product_list = mongo.get_list_product()
        pass

    def get_random_name(self):
        return random.choice(self.name_list)

    def get_random_product(self):
        return random.choice(self.product_list)
