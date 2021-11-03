from Domain.obiect2 import get_pret, get_descriere, creeaza_obiect, get_id, get_nume, get_locatie


def concatenare_string_descriere(lista_obiecte, cuv, valoare: float):
    """
    Concateneaza un string citit la descrierile obiectelor cu pretul mai mare decat o valoare citita
    :param lista_obiecte: lista din care luam obiectele
    :param cuv: string-ul pe care il concatenam descrierii unui obiect care indelineste proprietatea data
    :param valoare: valoarea pe care o comparam cu pretul de achizitie al unui obiect
    :return: lista cu obiectele al caror pret este mai amre decat valoare citita, iar la descriere a fost concatenat string-ul citit
    """
    new_list = []
    for obiect in lista_obiecte:
        if get_pret(obiect) > valoare:
            new_descriere = get_descriere(obiect) + cuv
            new_list.append(creeaza_obiect(get_id(obiect), get_nume(obiect), new_descriere, get_pret(obiect),
                                           get_locatie(obiect)))
        else:
            new_list.append(creeaza_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect),
                                           get_locatie(obiect)))
    return new_list




