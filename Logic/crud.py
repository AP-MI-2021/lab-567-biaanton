from Domain.obiect import creeaza_obiect, get_id


def create(lst_obiecte,id_obiect: int, nume, descriere, pret_achizitie, locatie):
    """
    Adaugarea unui obiect intr-o lista noua
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul de achizite al obiectului
    :param locatie: locatia obiectului
    :return: o noua lista formata din lst_obiecte si noul obiect adaugat
    """
    obiect=creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
    #lst_obiecte.append(obiect)
    return lst_obiecte + [obiect]


def read(lst_obiecte, id_obiect: int=None):
    """
    Citeste un obiect din "baza de date".
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului dorit
    :return: obiectul cu id-ul dorit sau lista cu toate obiectele, daca id-ul obiectului=None
    """
    obiectul_cu_id = None
    for obiect in lst_obiecte:
        if get_id(obiect) == id_obiect:
            obiectul_cu_id = obiect

    if obiectul_cu_id:
        return obiectul_cu_id
    return lst_obiecte


def update(lst_obiecte, new_obiect):
    """
    Actualizeaza un obiect.
    :param lst_obiecte: lista de obiecte
    :param obiect: obiectul care se va actualiza- id-ul trebuie sa fie existent
    :return: o lista cu obiectul actualizat.
    """
    new_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect)!= get_id(new_obiect):
            new_obiecte.append(obiect)
        else:
            new_obiecte.append(new_obiect)
    return new_obiecte


def delete(lst_obiecte, id_obiect: int):
    """
    Sterge un obiect
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului
    :return: o lista de obiecte fara obiectul cu id-ul id_obiect
    """
    new_obiecte = []
    for obiect in lst_obiecte:
        if get_id(obiect) != id_obiect:
            new_obiecte.append(obiect)

    return new_obiecte





