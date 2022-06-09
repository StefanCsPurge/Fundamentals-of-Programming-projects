

def createProd(name,price,quantity):
    return {'name': name,'price':price,'quantity':quantity}

def add_product(prod, prodList):
    prodList.append(prod)

def remove_prod(operator,price,prodList):
    """
        Function that removes the products by price
        :param operator: < or >
        :param price: int - the price to compare
        :param prodList: list - contains all the products up to this point
        :return: nothing. prodList will be updated
        """
    n = len(prodList)
    i = 0
    deleted = 0
    while i < n:
        if eval('{}{}{}'.format(prodList[i]['price'],operator,price)):
            deleted += 1
        else:
            prodList[i - deleted] = prodList[i]
        i += 1
    del prodList[n - deleted: n]

