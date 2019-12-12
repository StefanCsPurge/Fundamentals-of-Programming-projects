from operations import *
from operator import itemgetter

def print_animals(animalList):
    for animal in animalList:
        print("Code: {}, name: {}, type: {}, species: {}".format(animal['code'],animal['name'],animal['type'],animal['species']))

def print_menu():
    print("""Press:
    1 to add an animal to the collection
    2 to modify the type of an animal
    3 to change the type for a species
    4 to show all animals by type, sorted by name""")

def show_by_type(typ, animalList):
    selected_animals = select_by_type(typ, animalList)
    selected_animals = sorted(selected_animals, key=itemgetter('name'))
    print_animals(selected_animals)

def run():
    animals = [{'code':'Z01','name':'Alex','type':'herbivore','species':'zebra'},
               {'code':'Z02','name':'Ale','type':'herbivore','species':'zebra'},
               {'code':'Z03','name':'Almi','type':'omnivore','species':'bear'},
               {'code':'Z04','name':'Horea','type':'carnivore','species':'lion'},
               {'code':'Z05','name':'Mandinga','type':'herbivore','species':'zebra'}]
    print_menu()
    while True:
        opt = input('->')
        try:
            opt = opt.strip()
            if opt == '1':
                code = input('Insert code: ')
                name = input('Insert name: ')
                typ = input('Insert type: ')
                species = input('Insert species: ')
                animal = create_animal(code,name,typ,species)
                add_animal(animal,animals)
            elif opt == '2':
                code = input('Insert code of the animal to modify: ')
                newTyp = input('Insert the new type: ')
                modify_type(code.strip(),newTyp.strip(),animals)
                #print_animals(animals)
            elif opt == '3':
                species = input('Insert species: ')
                newTyp = input('Insert new type: ')
                modify_all_types(species,newTyp,animals)
                #print_animals(animals)
            elif opt == '4':
                typ = input('Insert type to show: ')
                show_by_type(typ.strip(),animals)
            elif opt == 'x':
                return
            else:
                raise Exception("Option does not exist!")
        except Exception as ex:
            print(ex)