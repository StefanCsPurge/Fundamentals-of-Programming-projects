from operations import *

def test_add_product():
    p1 = createProd('name1',123,3)
    p2 = createProd('name2',124,5)
    prodList = []
    add_product(p1,prodList)
    assert prodList == [p1]
    add_product(p2,prodList)
    assert prodList == [p1,p2]

def run_all_tests():
    test_add_product()