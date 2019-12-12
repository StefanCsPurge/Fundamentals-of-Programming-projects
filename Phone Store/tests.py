from operations import *

def test_phones_by_manufacturer():
    ph1 = createPhone('mnf1','mod1',10)
    ph2 = createPhone('mnf2', 'mod2', 20)
    ph3 = createPhone('mnf2', 'mod4', 50)
    phList = [ph1,ph2,ph3]
    newPhList = phones_by_manufacturer('mnf2',phList)
    assert newPhList == [ph2,ph3]
    newPhList = phones_by_manufacturer('mnf1', phList)
    assert newPhList == [ph1]

def run_all_tests():
    test_phones_by_manufacturer()