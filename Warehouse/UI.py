from operations import *
from operator import itemgetter

def list_products(products):
    for prod in products:
        print("Name: {}, price: {}, quantity: {}".format(prod['name'],prod['price'],prod['quantity']))

def call_add_prod(cmd,products):
    if len(cmd[1:]) != 3:
        raise Exception("Invalid command!")
    if not cmd[2].isdigit() or not cmd[3].isdigit() or int(cmd[2])<0 or int(cmd[3])<0:
        raise ValueError("Price and quantity are not positive integers!")
    name = str(cmd[1])
    quantity = int(cmd[2])
    price = int(cmd[3])
    product = createProd(name,price,quantity)
    add_product(product,products)

def call_remove_prod(cmd,products):
    remove_prod(cmd[1],cmd[2],products)

def list_price(prodList):
    sortedList = sorted(prodList, key=itemgetter('price'))
    list_products(sortedList)

def list_quantity(prodList):
    sortedList = sorted(prodList, key=itemgetter('quantity'))
    list_products(sortedList)

def run():
    products = [{'name': 'Napkins_pack_100','price':50,'quantity':22},
                {'name': 'Love_pack_100','price':100,'quantity':2},
                {'name': 'Cyka_pack_100','price':50,'quantity':100},
                {'name': 'Nig_pack_100','price':50,'quantity':20},
                {'name': 'PC_pack_100','price':9000,'quantity':2}]
    while True:
        cmd = input('Insert command> ')
        try:
            command = cmd.split()
            if command[0] == 'add':
                call_add_prod(command,products)
            elif command[0] == 'remove':
                call_remove_prod(command,products)
            elif command[0] == 'list':
                if command[1] == 'price':
                    list_price(products)
                elif command[1] == 'quantity':
                    list_quantity(products)
                else:
                    raise Exception("Incorrect command!")
            else:
                raise Exception("Command does not exist!")
        except Exception as ex:
            print(ex)