from Domain.obiect2 import get_pret


def get_ordonare_dupa_pret(lista_obiecte, undo_list: list, redo_list: list):
    """
    Ordoneaza obiectele dupa pretul de achizitie
    :param lista_obiecte: lista de obiecte ce urmeaza sa fie ordonate
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista cu obiectele ordonate dupa pretul de achizitie
    """
    undo_list.append(lista_obiecte)
    redo_list.clear()
    return sorted(lista_obiecte, key=get_pret)
