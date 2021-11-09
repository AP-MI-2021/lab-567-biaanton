from Domain.obiect2 import creeaza_obiect, get_id, get_locatie


def create(lst_obiecte, id_obiect: int, nume: str, descriere: str, pret_achizitie: float, locatie: str, undo_list: list, redo_list: list):
    """
    Adaugarea unui obiect intr-o lista noua
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul de achizite al obiectului
    :param locatie: locatia obiectului
    :param undo_list: lista de obiecte
    :param redo_list:
    :return: o noua lista formata din lst_obiecte si noul obiect adaugat
    """
    if read(lst_obiecte, id_obiect) is not None:
        raise ValueError(f'Exista deja un obiect cu id-ul {id_obiect}.')
    if len(locatie) != 4:
        raise ValueError(f'Locatia {locatie} nu are exact 4 caractere.')
    obiect = creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
    # lst_obiecte.append(obiect)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return lst_obiecte + [obiect]


def read(lst_obiecte, id_obiect: int):
    """
    Citeste un obiect din "baza de date".
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului dorit
    :param undo_list:
    :param redo_list:
    :return:
    -obiectul cu id-ul dorit, daca exista
    -lista cu toate obiectele, daca id-ul obiectului=None
    -None, daca nu exista un obiect cu id_obiect
    """
    if not id_obiect:
        return lst_obiecte
    obiectul_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiectul_cu_id = obiect
    if obiectul_cu_id:
        return obiectul_cu_id
    return None


def update(lst_obiecte, new_obiect, undo_list, redo_list):
    """
    Actualizeaza un obiect.
    :param lst_obiecte: lista de obiecte
    :param new_obiect: obiectul care se va actualiza- id-ul trebuie sa fie existent
    :param undo_list:
    :param redo_list:
    :return: o lista cu obiectul actualizat.
    """
    if read(lst_obiecte, get_id(new_obiect)) is None:
        raise ValueError(f'Nu exista un obiect cu id-ul {get_id(new_obiect)} pe care sa il actualizam')
    if len(get_locatie(new_obiect)) != 4:
        raise ValueError(f'Locatia {get_locatie(new_obiect)} nu are exact 4 caractere.')
    new_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != get_id(new_obiect):
            new_obiecte.append(obiect)
        else:
            new_obiecte.append(new_obiect)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return new_obiecte


def delete(lst_obiecte, id_obiect: int, undo_list: list, redo_list: list):
    """
    Sterge un obiect
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului
    :param undo_list:
    :param redo_list:
    :return: o lista de obiecte fara obiectul cu id-ul id_obiect
    """
    if read(lst_obiecte, id_obiect) is None:
        raise ValueError(f'Nu exista un obiect cu id-ul {id_obiect} pe care sa il stergem.')
    new_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != id_obiect:
            new_obiecte.append(obiect)
    undo_list.append(lst_obiecte)
    redo_list.clear()
    return new_obiecte





