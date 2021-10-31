from Domain.obiect2 import get_str, get_nume, get_descriere, get_locatie, get_pret, creeaza_obiect
from Logic.concatenare_string import concatenare_string_descriere
from Logic.crud import create, read, update, delete
from Logic.mutare_locatie import mutare_obiecte


def show_menu():
    print('1. CRUD')
    print('2. Mutarea obiectelor dintr-o locatie in alta')
    print('3. Concatenarea unui string la toate descrierile obiectelor cu pretul mai mare decat o valoare citita')
    #print('4. Determinarea celui mai mare pret petru fiecare locatie')
    #print('5. Ordonarea obiectelor crescator dupa pretul de achizitie')
    #print('6. Afisarea sumelor preturilor pentru fiecare locatie')
    #print('7. Undo')
    print('x. Exit')


def handle_add(obiecte):
    try:
        id_obiect = int(input('Dati id-ul obiectului: '))
        nume = input('Dati nume: ')
        descriere = input('Dati descrierea obiectului: ')
        pret_achizitie = int(input('Dati pretul de achizitie al obiectului: '))
        locatie = input('Dati locatia obiectului: ')
        return create(obiecte, id_obiect, nume, descriere, pret_achizitie, locatie)
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def handle_show_all(obiecte):
    for obiect in obiecte:
        print(get_str(obiect))


def handle_show_details(obiecte):
    try:
        id_obiect = int(input('Dati id-ul obiectului pentru care doriti detalii: '))
        obiect = read(obiecte, id_obiect)
        print(f'Nume: {get_nume(obiect)}')
        print(f'Descriere: {get_descriere(obiect)}')
        print(f'Pret achizitie: {get_pret(obiect)}')
        print(f'Locatie: {get_locatie(obiect)}')
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def handle_update(obiecte):
    try:
        id_obiect = int(input('Dati id-ul obiectului care se actualizeaza: '))
        nume = input('Dati noul nume: ')
        descriere = input('Dati noua descriere a obiectului: ')
        pret_achizitie = int(input('Dati noul pret de achizitie al obiectului: '))
        locatie = input('Dati noua locatie a obiectului: ')
        return update(obiecte, creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie))
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def handle_delete(obiecte):
    try:
        id_obiect = int(input('Dati id-ul obiectului care se va sterge: '))
        obiecte = delete(obiecte, id_obiect)
        print('Stergerea a fost efectuata cu succes.')
        return obiecte
    except ValueError as ve:
        print('Eroare: ', ve)
    return obiecte


def handle_crud(obiecte):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii obiect')
        print('r. Revenire')
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            obiecte = handle_update(obiecte)
        elif optiune == '3':
            obiecte = handle_delete(obiecte)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'r':
            break
        elif optiune == 'd':
            handle_show_details(obiecte)
        else:
            print('Optiune invalida.')
    return obiecte


def handle_mutare_locatie(obiecte):
    while True:
        print('1. Mutare obiecte dintr-o locatie in alta')
        print('a. Afisare')
        print('d. Detalii obiect')
        print('r. Revenire')
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            try:
                locatie1 = str(input('Dati locatia obiectelor pe care vreti sa le mutati'))
                locatie2 = str(input('Dati locatia unde vreti sa fie mutate obiectele'))
                obiecte = mutare_obiecte(obiecte, locatie1, locatie2)
                print(f'Mutarea obiectelor din locatia {locatie1} in {locatie2} a fost efectuata cu succes.')
            except ValueError as ve:
                print('Eroare: ', ve)
            return obiecte
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'r':
            break
        elif optiune == 'd':
            handle_show_details(obiecte)
        else:
            print('Optiune invalida.')
    return obiecte


def handle_concatenare_string(obiecte):
    while True:
        print('1. Concatenarea unui string citit la toate descrierile obiectelor cu pretul mai mare decat o '
              'valoare citita')
        print('a. Afisare')
        print('d. Detalii obiect')
        print('r. Revenire')
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            cuvant = str(input('Dati string-ul pe care il vom concatena la descrierea obiectelor '
                               'ce au pretul mai mare decat o valoare citita'))
            valoare = int(input('Dati valoare cu care vom compara pretul de achizitie'))
            obiecte = concatenare_string_descriere(obiecte, cuvant, valoare)
            print('Concatenarea string-ului a fost efectuata cu succes.')
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'r':
            break
        elif optiune == 'd':
            handle_show_details(obiecte)
        else:
            print('Optiune invalida.')
    return obiecte


def run_ui(obiecte):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            obiecte = handle_crud(obiecte)
        elif optiune == '2':
            obiecte = handle_mutare_locatie(obiecte)
        elif optiune == '3':
            obiecte=handle_concatenare_string(obiecte)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')
    return obiecte
