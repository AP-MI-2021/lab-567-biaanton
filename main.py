from Logic.crud import create
from Tests.test_concatenare_string import test_concatenare_string_descriere
from Tests.test_crud import test_crud
from Tests.test_mutare_locatie import test_mutare_locatie
from UserInterface.console import run_ui, show_menu
from UserInterface.console2 import run_ui2


def main():
    obiecte = []
    obiecte = create(obiecte, 1, 'imprimanta', 'performanta', 800, 'LOC4')
    obiecte = create(obiecte, 2, 'telefon', 'nou', 700, 'LOC4')
    obiecte = create(obiecte, 3, 'fax', 'bun', 400, 'LOC5')
    obiecte = create(obiecte, 4, 'caiet', 'A4', 4, 'LOC2')
    print('1. Meniu initial')
    print('2. Meniu nou')
    optiune = input('Alegeti meniul dorit')
    if optiune == '1':
        obiecte = run_ui(obiecte)
    else:
        obiecte= run_ui2(obiecte)

if __name__ == '__main__':
    test_crud()
    test_mutare_locatie()
    test_concatenare_string_descriere()
    main()

