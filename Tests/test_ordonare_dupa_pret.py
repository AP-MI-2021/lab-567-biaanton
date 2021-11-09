from Domain.obiect2 import creeaza_obiect
from Logic.ordonare_dupa_pret import get_ordonare_dupa_pret


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC2'),
            creeaza_obiect(3, 'o3', 'desc3', 0, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
            ]


def test_ordonare_dupa_pret():
    obiecte = get_data()
    obiecte = get_ordonare_dupa_pret(obiecte, [], [])
    assert obiecte[0] == get_data()[2]
    assert obiecte[1] == get_data()[4]
    assert obiecte[4] == get_data()[3]