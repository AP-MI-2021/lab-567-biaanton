from Domain.obiect2 import get_locatie, get_pret


def get_sume_preturi_locatie(lista_obiecte):
    """
    Determina sumele preturilor pentru fiecare locatie
    :param lista_obiecte: lista de obiecte
    :return: un dictionar in care cheia este locatia si valoarea este suma preturilor din acea locatie
    """
    result = {}
    for obiect in lista_obiecte:
        locatie = get_locatie(obiect)
        if locatie not in result:
            result[locatie] = get_pret(obiect)
        else:
            result[locatie] = result[locatie] + get_pret(obiect)
    return result
