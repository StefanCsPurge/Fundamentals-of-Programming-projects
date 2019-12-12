from operations import *

def test_add_animal():
    a1 = create_animal('c1','name1','type1','species1')
    a2 = create_animal('c2','name2','type2','species2')
    a3 = create_animal('c3', '', 'type3', 'species2')
    a4 = create_animal('c4', 'otherName', 'type3', ' ')
    a5 = create_animal('c1', 'name5', 'type5', 'species5')
    animalList = []
    add_animal(a1,animalList)
    assert animalList == [a1]
    add_animal(a2,animalList)
    assert animalList == [a1,a2]
    try:
        add_animal(a3,animalList)
        assert False
    except Exception:
        assert True
    try:
        add_animal(a4,animalList)
        assert False
    except Exception:
        assert True
    try:
        add_animal(a5,animalList)
        assert False
    except Exception:
        assert True

def test_modify_type():
    a1 = create_animal('c1', 'name1', 'type1', 'species1')
    a2 = create_animal('c2', 'name2', 'type2', 'species2')
    a3 = create_animal('c3', 'name3', 'type3', 'species4')
    Na2 = create_animal('c2', 'name2', 'nTyp1', 'species2')
    Na3 = create_animal('c3', 'name3', 'nTyp3', 'species4')
    animalList = [a1,a2,a3]
    modify_type('c2','nTyp1',animalList)
    assert animalList == [a1,Na2,a3]
    modify_type('c3', 'nTyp3', animalList)
    assert animalList == [a1,Na2,Na3]


def run_all_tests():
    test_add_animal()
    test_modify_type()