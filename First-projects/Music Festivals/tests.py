from operations import *

def test_add_festival():
    festList = []
    f1 = createFestival("fest1",12,123,['art1','art2'])
    f2 = createFestival("fest2", 11, 153, ['art1', 'art2'])
    fBad = createFestival("fest2", 120, 153, ['art1', 'art2'])
    add_festival(f1,festList)
    assert (festList == [f1])
    add_festival(f2,festList)
    assert (festList == [f1,f2])
    try:
        add_festival(f2, festList)
        add_festival(fBad,festList)
        add_festival(f1,festList)
        assert False
    except Exception:
        assert True

def test_select_fest_by_artist():
    f1 = createFestival("fest1", 12, 123, ['art1', 'art2'])
    f2 = createFestival("fest2", 11, 153, ['art33', 'art2'])
    festList = [f1,f2]
    festList2 = select_fest_by_artist('art33',festList)
    assert festList2 != festList
    assert festList2 == [f2]

def run_all_tests():
    test_add_festival()
    test_select_fest_by_artist()