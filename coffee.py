class Coffee:
    def init(self, name):
        self._name = None
        self.name = name 
    @property
    def name(self):
        return self._name

@name.setter
def name(self, value):
    if not isinstance(value, str):
        raise TypeError("Name must be a string")
    if len(value) < 3:
        raise ValueError("Name must be at least 3 characters long")
    self._name = value

def orders(self):
    return [order for order in Order._all_orders if order.coffee is self]

def customers(self):
    return list({order.customer for order in self.orders()})

def num_orders(self):
    return len(self.orders())

def average_price(self):
    all_orders = self.orders()
    if not all_orders:
        return 0
    total_price = sum(order.price for order in all_orders)
    return total_price / len(all_orders)