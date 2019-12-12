from operations import *

def print_phones(phoneList):
    for phone in phoneList:
        print("Manufacturer: {}, model: {}, price: {}".format(phone['mnf'],phone['model'],phone['price']))

def find_from_mnf(mnf, phoneList):
    selected_phones = phones_by_manufacturer(mnf,phoneList)
    print_phones(selected_phones)

def print_menu():
    print("""Press:
    1 to add a phone
    2 to find phones from a manufacturer
    3 to increase the price of a phone
    4 to increase the price of all phones with percent""")
def run():
    phoneList = [{'mnf':'Samsung', 'model':'S22', 'price':9000},
          {'mnf':'Apple', 'model':'IPh 34', 'price':10000},
          {'mnf':'Motorola', 'model':'3234', 'price':300},
          {'mnf':'OnePlus', 'model':'45565', 'price':444},
          {'mnf':'Nokia','model':'1311','price':420}]
    print_menu()
    while True:
        opt = input('->')
        try:
            opt = opt.strip()
            if opt == '1':
                mnf = input('Insert manufacturer: ')
                model = input('Insert model: ')
                price = int(input("Insert price: "))
                phone = createPhone(mnf.strip(),model.strip(),price)
                add_phone(phone,phoneList)
            elif opt == '2':
                mnf = input('Insert manufacturer: ')
                find_from_mnf(mnf.strip(),phoneList)
            elif opt == '3':
                mnf = input('Insert manufacturer: ')
                model = input('Insert model: ')
                amount = int(input("Insert amount to add: "))
                update_price(mnf.strip(),model,amount,phoneList)
            elif opt == '4':
                percent = int(input("Insert percent: "))
                update_all_percentage(percent, phoneList)
            elif opt == '5':
                print_phones(phoneList)
            else:
                raise Exception("Option does not exist!")
        except Exception as ex:
            print(ex)