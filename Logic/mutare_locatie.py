from Domain.obiect2 import get_locatie, creeaza_obiect, get_id, get_nume, get_descriere, get_pret


def mutare_obiecte(lista_obiecte, locatie1, locatie2, undo_list: list, redo_list: list):
    """
    Muta obiectele dintr-o anumita locatie in alta
    :param lista_obiecte: lista din care luam obiectele
    :param locatie1: locatia din care dorim sa mutam toate obiectele
    :param locatie2: locatia unde mutam obiectele
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista noua
    """
    if len(locatie1) != 4:
        raise ValueError(f'Locatia {locatie1} nu are exact 4 caractere.')
    if len(locatie2) != 4:
        raise ValueError(f'Locatia {locatie2} nu are exact 4 caractere.')
    new_list = []
    for obiect in lista_obiecte:
        if locatie1 == get_locatie(obiect):
            new_loc = locatie2
            new_list.append(creeaza_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect),
                                           new_loc))
        else:
            new_list.append(creeaza_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect),
                                           get_locatie(obiect)))
    undo_list.append(lista_obiecte)
    redo_list.clear()
    return new_list














