from Domain.obiect2 import creeaza_obiect, get_locatie
from Logic.mutare_locatie import mutare_obiecte


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC2'),
            creeaza_obiect(3, 'o3', 'desc3', 0, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
            ]


def test_mutare_locatie():
        obiecte = get_data()
        locatie_veche = 'LOC4'
        locatie_noua = 'LOC1'
        new_obiecte = mutare_obiecte(obiecte, locatie_veche, locatie_noua)
        assert get_locatie(obiecte[4]) != get_locatie(new_obiecte[4])
        assert get_locatie(obiecte[3]) != get_locatie(new_obiecte[3])
        assert get_locatie(obiecte[0]) == get_locatie(new_obiecte[0])







