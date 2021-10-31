from Domain.obiect2 import creeaza_obiect, get_id, get_locatie
from Logic.crud import create, read, update, delete


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC2'),
            creeaza_obiect(3, 'o3', 'desc3', 0, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
    ]


def test_create():
    obiecte = get_data()
    params = (20, 'onew', 'desc new', 2154.5, 'LOC4')
    o_new = creeaza_obiect(*params)
    new_obiecte = create(obiecte, *params)
    assert len(new_obiecte) == len(obiecte) + 1
    assert o_new in new_obiecte

    # testam daca se lanseaza exceptie pentru id duplicat
    params2 = (20, 'scaun', 'vdfvj', 325, 'LOC2')
    try:
        some_o = create(new_obiecte, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    obiecte = get_data()
    some_o = obiecte[2]
    assert read(obiecte, get_id(some_o)) == some_o
    assert read(obiecte, None) == obiecte


def test_update():
    obiecte = get_data()
    o_updated = creeaza_obiect(1, 'new name', 'new desc', 111, 'LOC3')
    updated = update(obiecte, o_updated)
    assert o_updated in updated
    assert o_updated not in obiecte
    assert len(updated) == len(obiecte)


def test_delete():
    obiecte = get_data()
    to_delete = 3
    o_deleted = read(obiecte, to_delete)
    deleted = delete(obiecte, to_delete)
    assert o_deleted not in deleted
    assert o_deleted in obiecte
    assert len(deleted) == len(obiecte)-1


def test_crud():
    test_create()
    test_read()
    test_delete()












