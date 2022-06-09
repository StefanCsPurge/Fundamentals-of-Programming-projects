
def create_animal(code,name,typ,species):
    return {'code':code,'name':name,'type':typ,'species':species}

def add_animal(animal,animalList):
    """
    Function that adds an animal to the animal collection.
    :param animal: dictionary - the animal to add
    :param animalList: list of dictionaries - the animal collection
    :return: nothing
    raise errors if the new animal has a void field or the code is already used
    """
    if animal['code'].strip == '' or animal['name'].strip == '' or animal['type'].strip == '' or animal['species'].strip == '':
        raise ValueError('Animal has a void field!')
    for a in animalList:
        if a['code'] == animal['code']:
            raise Exception('Code is already used!')
    animalList.append(animal)

def modify_type(code,newType,animalList):
    """
    Function that modifies the type of a given animal.
    :param code: str - the animal code
    :param newType: str - the new type to modify with
    :param animalList: list of dictionaries (animals)
    :return: nothing
    """
    for animal in animalList:
        if animal['code'] == code:
            animal['type'] = newType
            break

def modify_all_types(species,newType,animalList):
    if newType.strip() == '':
        raise ValueError('The new type is void!')
    for animal in animalList:
        if animal['species'] == species:
            animal['type'] = newType

def select_by_type(typ, animalList):
    newAnimalList = []
    for animal in animalList:
        if animal['type'] == typ:
            newAnimalList.append(animal)
    return newAnimalList