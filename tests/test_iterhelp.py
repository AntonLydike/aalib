from aalib.iterhelp import split_at

def test_split_at():
    data = range(0, 10)

    assert split_at(lambda x: x >= 3, data) == (range(0,3), range(3,10))
    assert split_at(lambda x: x == 0, data) == (range(0,0), range(0,10))
    assert split_at(lambda x: x > 100, data) == (range(0,10), ())
