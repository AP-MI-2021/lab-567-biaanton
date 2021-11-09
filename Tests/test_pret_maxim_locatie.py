from Domain.obiect2 import creeaza_obiect, get_pret, get_str
from Logic.pret_maxim_locatie import get_pret_maxim_locatie


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC1'),
            creeaza_obiect(3, 'o3', 'desc3', 10, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
            ]


def test_pret_maxim_locatie():
    obiecte = get_data()
    result = get_pret_maxim_locatie(obiecte)
    assert get_pret(result['LOC1']) == 100
    assert get_pret(result['LOC3']) == 10
    assert get_pret(result['LOC4']) == 145421


