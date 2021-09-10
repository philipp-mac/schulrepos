def all_bigger_five(liste):
    if type(liste) is not list:
        return False
    elif len(liste) == 0:
        return False
        
    for item in liste:
        if type(item) is not int or type(item) is not float:
            return False
        if item < 6:
            return False
    return True

def test_all_bigger_five():
    assert not all_bigger_five([1,2])
    assert not all_bigger_five("String")
    assert not all_bigger_five(1)
    assert not all_bigger_five([6, "hello"])
    assert not all_bigger_five([])
    assert not all_bigger_five(None)
    assert not all_bigger_five(object)
    assert not all_bigger_five([6, 7, 4])
    assert all_bigger_five([6, 7, 8])


test_all_bigger_five()