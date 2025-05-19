 from customer import Customer;
from coffee import Coffee;

class Order:
    def __init__(self, customer, coffee, price):
        self.customer =customer
        self.coffee = coffee
        self.price = float(price)

if __name__ == "__main__":
  
    customer = Customer("William")
    coffee = Coffee("urife")

    customer1 = Customer("Nancy")
    coffee1 = Coffee("lafder")

    order = customer.create_order(coffee, 3.50)
    order1 = customer1.create_order(coffee1, 4.50)
    print("********")

    aficionado = Customer.most_aficionado(order.coffee)
    if aficionado:
        print(f"The most aficionado for {coffee.name} is: {aficionado.name}")
    else:
        print(f"No aficionado found for {coffee.name}.")

    print("*** ***")

    print(f"Order created by: {order.customer.name}")
    print(f"Coffee: {order.coffee.name}, Price: ${order.price}") 
    print("*** ***")
    print(f"Order created by: {order1.customer.name}")
    print(f"Coffee: {order1.coffee.name}, Price: ${order1.price}")