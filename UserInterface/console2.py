from Domain.obiect2 import creeaza_obiect, get_str
from Logic.concatenare_string import concatenare_string_descriere
from Logic.crud import create, update, delete
from Logic.mutare_locatie import mutare_obiecte


def help_menu():
    print('Exemplu:')
    print('-Pentru CRUD')
    print('     -Adaugare: add, id_obiect, nume, descriere, pret_achizitie, locatie ')
    print('     -Actualizare: update, id_obiect, nume, descriere, pret_achizitie, locatie ')
    print('     -Stergere: delete, id_obiect')
    print('-Pentru afisarea obiectelor: show_all')
    print('-Pentru mutarea obiectelor dintr-o locatie in alta: mutare, locatie_veche, locatie_noua')
    print('-Pentru concatenarea unui string citi la descrierea obiectelor care au pretul de achizitie mai mare decat '
          'o valoare citia: concatenare, string, valoare')
    print('-Pentru a folosi mai multe instructiuni la o singura citire: add, id_obiect, nume, descriere, '
          'pret_achizitie, locatie; show_all; mutare, locatie_veche, locatie_noua; concatenare, string, valoare')


def run_ui2(obiecte):
    while True:
        option = input('Dati instructiunile dorite. Pentru ajutor, introduceti "help". Pentru iesire, introduceti "x".')
        if option == 'help':
            help_menu()
        elif option == 'x':
            break
        else:
            instructiuni = option.split(';')
            for elemente in instructiuni:
                comenzi = elemente.split(',')
                if comenzi[0] == 'add':
                    try:
                        obiecte = create(obiecte, int(comenzi[1]), comenzi[2], comenzi[3], float(comenzi[4]), comenzi[5])
                    except ValueError as ve:
                        print('Eroare: ', ve)
                elif comenzi[0] == 'update':
                    try:
                        obiect_nou = creeaza_obiect(int(comenzi[1]), comenzi[2], comenzi[3], float(comenzi[4]), comenzi[5])
                        obiecte = update(obiecte, obiect_nou)
                    except ValueError as ve:
                        print('Eroare: ', ve)
                elif comenzi[0] == "delete":
                    try:
                        obiecte = delete(obiecte, int(comenzi[1]))
                    except ValueError as ve:
                        print('Eroare: ', ve)
                elif comenzi[0] == "mutare":
                    try:
                        obiecte = mutare_obiecte(obiecte, comenzi[1], comenzi[2])
                    except ValueError as ve:
                        print('Eroare: ', ve)
                elif comenzi[0] == "concatenare":
                    try:
                        obiecte = concatenare_string_descriere(obiecte, comenzi[1], float(comenzi[2]))
                    except ValueError as ve:
                        print('Eroare: ', ve)
                elif comenzi[0] == 'show_all':
                    for obiect in obiecte:
                        print(get_str(obiect))
                else:
                    print('Optiune invalida.')





