import pymongo as mg


class Communnicator:
    mongo = ''
    product_list = []
    name_list = []

    def __init__(self, product_set_name):
        self.mongo = mg.MongoClient("localhost", 27017)
        name_list = self.mongo['vietnam_name']['full_name'].find({}, {'_id': 0, 'full_name': 1})
        product_list = self.mongo[product_set_name]['product'].find({}, {'_id': 0})
        for name in name_list:
            self.name_list.append(name['full_name'])
        for product in product_list:
            self.product_list.append(product)
        pass

    def get_list_name(self):
        return self.name_list

    def get_list_product(self):
        return self.product_list

