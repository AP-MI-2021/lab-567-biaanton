from Domain.obiect2 import get_pret


def get_ordonare_dupa_pret(lista_obiecte):
    """
    Ordoneaza obiectele dupa pretul de achizitie
    :param lista_obiecte: lista de obiecte ce urmeaza sa fie ordonate
    :return: lista cu obiectele ordonate dupa pretul de achizitie
    """
    return sorted(lista_obiecte, key=get_pret)
