from Domain.obiect2 import get_pret, get_descriere, creeaza_obiect, get_id, get_nume, get_locatie


def concatenare_string_descriere(lista_obiecte, cuv, valoare: float):
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




