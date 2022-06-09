def createProd(name,price,quantity):
    return {'name': name,'price':price,'quantity':quantity}

def add_product(prod, prodList):
    """
    Function that adds a product to the product list
    :param prod: dictionary - my new product
    :param prodList: list of dictionaries
    :return: nothing. Prod list will be updated.
    """
    prodList.append(prod)

def remove_prod(name,prodList):
    ok = False
    for prod in prodList:
        if prod['name'] == name:
            prodList.remove(prod)
            ok = True
            break
    if ok is False:
        raise Exception('The product by this name does not exist!')

def calculate_total_value(prodList):
    total = 0
    for prod in prodList:
        total += prod['price']*prod['quantity']
    return total