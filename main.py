from Logic.crud import create
from Tests.test_concatenare_string import test_concatenare_string_descriere
from Tests.test_crud import test_crud
from Tests.test_mutare_locatie import test_mutare_locatie
from UserInterface.console import run_ui


def main():
    obiecte = []
    obiecte = create(obiecte, 1, 'imprimanta', 'performanta', 800, 'LOC4')
    obiecte = create(obiecte, 2, 'telefon', 'nou', 700, 'LOC4')
    obiecte = create(obiecte, 3, 'fax', 'bun', 400, 'LOC5')
    obiecte = create(obiecte, 4, 'caiet', 'A4', 4, 'LOC2')
    obiecte = run_ui(obiecte)

if __name__ == '__main__':
    test_crud()
    test_mutare_locatie()
    test_concatenare_string_descriere()
    main()

