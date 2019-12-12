from operations import *

def test_remove_product():
    p1 = createProd('Name1',111,12)
    p2 = createProd('Name2',122,33)
    p3 = createProd('name3',234,34)
    prodList = [p1,p2,p3,p1]
    remove_prod('>',200,prodList)
    assert prodList == [p1,p2,p1]
    remove_prod('<',122,prodList)
    assert prodList == [p2]
    remove_prod('>',0,prodList)
    assert prodList == []


def run_all_tests():
    test_remove_product()