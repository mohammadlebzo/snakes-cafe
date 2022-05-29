orders_customer = {}
orders_available = ('wings', 'cookies', 'spring rolls', 'salmon'
                    , 'steak', 'meat tornado', 'a literal garden'
                    , 'ice cream', 'cake', 'pie', 'coffee', 'tea'
                    , 'unicorn tears')


def main_message():
    return """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************"""


def order_handler(order):
    if order.lower() in orders_available:
        if order.lower() in orders_customer:
            orders_customer[order.lower()] += 1
            return f'   **{orders_customer[order.lower()]} orders of {order} have been added to your meal**'
        else:
            orders_customer[order.lower()] = 1
            return f'   **{orders_customer[order.lower()]} order of {order} have been added to your meal**'
    else:
        return '    Item not available, please enter one of the items in the list above ^'


def program_handler():
    print(main_message())
    choice = input("    > ")
    while choice != 'quit':
        print(order_handler(choice))
        choice = input("    > ")


program_handler()
