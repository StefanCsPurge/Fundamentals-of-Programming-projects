
def createPhone(manufacturer, model, price):
    return {'mnf':manufacturer, 'model':model, 'price':price}

def add_phone(phone,phoneList):
    if len(phone['mnf'])<3 or len(phone['model'])<3 or len(str(phone['price']))<3:
        raise ValueError("Invalid phone!")
    phoneList.append(phone)

def phones_by_manufacturer(mnf,phoneList):
    """
    Function that selects only the phones from a given manufacturer.
    :param mnf: str - the name of the manufacturer
    :param phoneList: - list of dictionaries = phones
    :return: nothing
    """
    selectedPhones = []
    for phone in phoneList:
        if phone['mnf'] == mnf:
            selectedPhones.append(phone)
    return selectedPhones

def update_price(mnf,model,amount,phoneList):
    ok = False
    for phone in phoneList:
        if phone['mnf'] == mnf and phone['model'] == model:
            phone['price'] += amount
            ok = True
    if ok is False:
        raise Exception("There is no phone like this!")

def compute_percentage(percent,x):
    return x*percent/100

def update_all_percentage(percentage, phoneList):
    if percentage < -50 or percentage > 100:
        raise ValueError("Percent value is not within the required bounds!")
    for phone in phoneList:
        phone['price'] += compute_percentage(percentage,phone['price'])
