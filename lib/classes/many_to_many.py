class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) <= 2:
            raise ValueError("Name length must be greater than 2 characters")

        self._name = name
        self._orders = []  # Initialize list to store orders
        self._customers = set()  # Initialize set to store unique customers

    @property
    def name(self):
         return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(self._customers)  # Convert set to list for compatibility

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Order must be an instance of Order")
        self._orders.append(order)
        self._customers.add(order.customer)  # Add the customer to the coffee's customers set

    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a type of string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Length of the name should be between 1 and 15 characters")
        self.name = name  # Updated to make name mutable
        self._orders = []

    def orders(self):
        return self._orders

    def coffees(self):
        coffee_list = []
        for order in self._orders:
            coffee_list.append(order.coffee)
        return coffee_list

    def create_order(self, coffee, price):
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order




class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee")
        self.customer = customer
        self.coffee = coffee
        self._price = price
        self.coffee.orders().append(self) 
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    def _set_price(self, value):
        raise AttributeError("Price is immutable")

    price = property(price, _set_price)