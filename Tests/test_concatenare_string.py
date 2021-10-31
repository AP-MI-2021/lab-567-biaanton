from Domain.obiect2 import creeaza_obiect, get_descriere
from Logic.concatenare_string import concatenare_string_descriere


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC2'),
            creeaza_obiect(3, 'o3', 'desc3', 0, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
            ]


def test_concatenare_string_descriere():
    cuvant= "SCHIMBAT"
    obiecte = get_data()
    valoare = 50
    new_obiecte = concatenare_string_descriere(obiecte, cuvant, valoare)
    assert get_descriere(obiecte[0]) != get_descriere(new_obiecte[0])
    assert get_descriere(obiecte[4]) == get_descriere(new_obiecte[4])
    assert get_descriere(obiecte[3]) != get_descriere(new_obiecte[3])
