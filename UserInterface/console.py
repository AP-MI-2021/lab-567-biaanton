from Domain.obiect2 import get_str, get_nume, get_descriere, get_locatie, get_pret, creeaza_obiect
from Logic.crud import create, read, update, delete


def show_menu():
    print('1. CRUD')
    print('2. Mutarea obiectelor dintr-o locatie in alta')
    print('3. Concatenarea unui string la toate descrierile obiectelor cu pretul mai amre decat o valoare citita')
    print('4. Determinarea celui mai mare pret petru fiecare locatie')
    print('5. Ordonarea obiectelor crescator dupa pretul de achizitie')
    print('6. Afisarea sumelor preturilor pentru fiecare locatie')
    print('7. Undo')
    print('x. Exit')


def handle_add(obiecte):
    id_obiect = int(input('Dati id-ul obiectului: '))
    nume = input('Dati nume: ')
    descriere = input('Dati descrierea obiectului: ')
    pret_achizitie = int(input('Dati pretul de achizitie al obiectului: '))
    locatie = input('Dati locatia obiectului: ')
    return create(obiecte, id_obiect, nume, descriere, pret_achizitie, locatie)


def handle_show_all(obiecte):
    for obiect in obiecte:
        print(get_str(obiect))


def handle_show_details(obiecte):
    id_obiect = int(input('Dati id-ul obiectului pentru care doriti detalii: '))
    obiect = read(obiecte, id_obiect)
    print(f'Nume: {get_nume(obiect)}')
    print(f'Descriere: {get_descriere(obiect)}')
    print(f'Pret achizitie: {get_pret(obiect)}')
    print(f'Locatie: {get_locatie(obiect)}')


def handle_update(obiecte):
    id_obiect = int(input('Dati id-ul obiectului care se actualizeaza: '))
    nume = input('Dati noul nume: ')
    descriere = input('Dati noua descriere a obiectului: ')
    pret_achizitie = int(input('Dati noul pret de achizitie al obiectului: '))
    locatie = input('Dati noua locatie a obiectului: ')
    return update(obiecte,creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie))


def handle_delete(obiecte):
    id_obiect = int(input('Dati id-ul obiectului care se va sterge: '))
    obiecte = delete(obiecte,id_obiect)
    print('Stergerea a fost efectuata cu succes.')
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

def run_ui(obiecte):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            obiecte = handle_crud(obiecte)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')


    return obiecte
