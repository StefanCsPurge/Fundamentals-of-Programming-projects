from services import *

def test_student_add():
    """
    Test the first functionality: adding a student to the list.
    """
    testSrv = Services()
    stud1 = Student(1,"Gigel1", 2)
    stud2 = Student(22,'Gigel2',33)
    testSrv.add_student(stud1)
    assert testSrv.getStudList() == [stud1]
    testSrv.add_student(stud2)
    assert testSrv.getStudList() == [stud1,stud2]
    try:
        testSrv.add_student(Student(22,"Gigel2",33))
        testSrv.add_student(stud1)
        assert False
    except Exception:
        assert True

"""
name_list = ['Gigel Frone',
             'Maria Magdalena',
             'Chinezu Nou',
             'The Bucuria',
             'John Lennon',
             'Ma Ni99a',
             'Alexandrion',
             'Bossu Coltuneac',
             'Diana Norocoasa',
             'Ana Fratelo',
             'Ion Agarbiceanu']
random_name_list = [names.get_full_name() for i in range(10)]
print(random_name_list)
random_name_list.clear()
for i in range(10):
    random_name_list.append(names.get_full_name())
print(random_name_list)
print(random.random())
print(random.choice(name_list))
print(random.randint(0,100))
random.shuffle(name_list)
print(name_list)
"""
