from Domain.obiect2 import creeaza_obiect
from Logic.sume_preturi_locatie import get_sume_preturi_locatie


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC1'),
            creeaza_obiect(3, 'o3', 'desc3', 10, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
            ]


def test_sume_preturi_locatie():
    obiecte = get_data()
    result = get_sume_preturi_locatie(obiecte)
    assert result['LOC1'] == 160
    assert result['LOC3'] == 10
    assert result['LOC4'] == 145441.87
