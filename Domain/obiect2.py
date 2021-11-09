def creeaza_obiect(id_obiect: int, nume, descriere, pret_achizitie, locatie):
    """
    Creeaza o lista cu detaliile obiectului.
    :param id_obiect: id-ul obiectului, trebuie sa fie unic
    :param nume: numele obiectului, nenul
    :param descriere: descrierea obiectului, nenul
    :param pret_achizitie: pretul de achizitie al obiectului
    :param locatie: locatia obiectului, exact 4 caractere
    :return: lista cu detaliile obiectului
    """
    lista_obiect=[id_obiect,nume,descriere,pret_achizitie,locatie]
    return lista_obiect


def get_id(lista_obiect):
    """
    Getter pentru id-ul obiectului
    :param lista_obiect: lista din care extragem id-ul obiectului
    :return: id-ul obiectului
    """
    return lista_obiect[0]


def get_nume(lista_obiect):
    """
    Getter pentru numele obiectului
    :param lista_obiect: lista din care extragem numele obiectului
    :return: numele obiectului
    """
    return lista_obiect[1]


def get_descriere(lista_obiect):
    """
    Getter pentru descrierea obiectului
    :param lista_obiect: lista din care extragem descrierea obiectului
    :return: descrierea obiectului
    """
    return lista_obiect[2]


def get_pret(lista_obiect):
    """
    Getter pentru pretul de achizitie al obiectului
    :param lista_obiect: lista din care extragem pretul de achizitie al obiectului
    :return: pretul de achizitie al obiectului
    """
    return lista_obiect[3]


def get_locatie(lista_obiect):
    """
     Getter pentru locatia obiectului
    :param lista_obiect: lista din care extragem locatia obiectului
    :return: locatia obiectului
    """
    return lista_obiect[4]


def get_str(lista_obiect):
    return f'Obiectul cu id-ul {get_id(lista_obiect)}, aflat in locatia {get_locatie(lista_obiect)}, pretul {get_pret(lista_obiect)}, numele {get_nume(lista_obiect)}, descriere {get_descriere(lista_obiect)}'

