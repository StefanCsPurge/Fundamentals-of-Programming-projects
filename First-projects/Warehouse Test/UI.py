from operations import *

def list_products(products):
    for prod in products:
        print("Name: {}, price: {}, quantity: {}".format(prod['name'],prod['price'],prod['quantity']))

def call_add_prod(cmd, products):
    if len(cmd[1:]) != 3:
        raise Exception("Invalid cmd!")
    if not cmd[2].isdigit() or not cmd[3].isdigit() or int(cmd[2]) < 0 or int(cmd[3]) < 0:
        raise ValueError("Price and quantity aren't positive int!")
    name = str(cmd[1])
    quantity = int(cmd[2])
    price = int(cmd[3])
    product = createProd(name, price, quantity)
    add_product(product, products)

def call_remove_prod(cmd, products):
    name = cmd[1]
    remove_prod(name, products)

def run():
    products = [{'name':'nap_pack10','price':50,'quantity':2},
                {'name':'van','price':10,'quantity':3},
                {'name':'bodies','price':20,'quantity':100},
                {'name':'blunts','price':420,'quantity':420},
                {'name':'PC','price':10,'quantity':2}]
    while True:
        cmd = input("Insert command > ")
        try:
            command = cmd.split()
            if command[0] == 'add':
                call_add_prod(command,products)
            elif command[0] == 'remove':
                call_remove_prod(command,products)
            elif command[0] == 'list':
                if command[1] == 'all':
                    list_products(products)
                elif command[1] == 'total':
                    print("The total value of products in the warehouse is {} RON".format(calculate_total_value(products)))
                else:
                    raise Exception('Invalid cmd!')
            elif command[0] == 'exit':
                return
            else:
                raise Exception("Command does not exist!")
        except Exception as msg:
            print(msg)