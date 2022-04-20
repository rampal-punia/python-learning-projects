def get_pizza_order(order_num, size, *args, **kwargs):
    print(f"=====================================")
    print(f"Order number: {order_num}")
    print(f"Preparing pizza with size {size} inches.")

    print("Adding the following toppings to the pizza.")
    for topping in args:
        print(f" - {topping}")

    for k, v in kwargs.items():
        print(f"{k} : {v}")
    print(f"=====================================")


toppings = ('green chilly', 'mushroom', 'extra cheese',
            'extra paneer', 'Italian sausage', 'pepperoni')

order_3 = get_pizza_order(
    111, 10, 'green chilly', 'Italian sausage', delivery_type="Home", address="#71, abc road")
order_4 = get_pizza_order(
    112, 7, 'green chilly', 'mushroom', 'extra cheese', delivery_type="table", table_number=12)
