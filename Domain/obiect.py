def creeaza_obiect(id_obiect: int, nume, descriere, pret_achizitie, locatie):
    """
    Creeaza un obiect.
    :param id_obiect: id-ul obiectului, trebuie sa fie unic
    :param nume: numele obiectului, nenul
    :param descriere: descrierea obiectului, nenul
    :param pret_achizitie: pretul de achizitie al obiectului
    :param locatie: locatia obiectului, exact 4 caractere
    :return: un obiect
    """
    return {
        'id': id_obiect,
        'nume': nume,
        'desc': descriere,
        'pret': pret_achizitie,
        'locatie': locatie,
    }


def get_id(obiect):
    """
    Getter pentru id-ul obiectului.
    :param obiect: obiectul
    :return: id-ul obiectului dat ca parametru
    """
    return obiect['id']


def get_nume(obiect):
    """
    Getter pentru numele obiectului
    :param obiect: obiectul
    :return: numele obiectului dat ca parametru
    """
    return obiect['nume']


def get_descriere(obiect):
    """
    Getter pentru descrierea obiectului
    :param obiect: obiectul
    :return: descrierea obiectului data ca parametru
    """
    return obiect['desc']


def get_pret(obiect):
    """
    Getter pentru pretul de achizitie al obiectului
    :param obiect: obiectul
    :return: pretul de ahizitie al obiectului dat ca parametru
    """
    return obiect['pret']


def get_locatie(obiect):
    """
    Getter pentru locatia obiectului
    :param obiect: obiectul
    :return: locatia obiectului data ca paramaetru
    """
    return obiect['locatie']


def get_str(obiect):
    return f'Obiectul cu id-ul {get_id(obiect)}, aflat in locatia {get_locatie(obiect)}, pretul {get_pret(obiect)},' \
           f'numele {get_nume(obiect)}, descriere {get_descriere(obiect)}'
