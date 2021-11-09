from Domain.obiect2 import get_locatie, get_pret


def get_pret_maxim_locatie(obiecte):
    """
    Determina pretul maxim din fiecare locatie
    :param obiecte: lista de obiecte pe care o vom folosi pentru a afla pretul maxim din fiecare locatie
    :return: un dictionare in care cheia este locatia si valoarea este obiectul cu pretul maxim din acea locatie
    """
    result = {} # result[x] = obiectul cu pretul maxim din locatia x
    for obiect in obiecte:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie not in result:
            result[locatie] = obiect
        else:
            if pret > get_pret(result[locatie]):
                result[locatie] = obiect
    return result









