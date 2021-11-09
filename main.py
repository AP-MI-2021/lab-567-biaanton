from Logic.crud import create
from Tests.test_concatenare_string import test_concatenare_string_descriere
from Tests.test_crud import test_crud
from Tests.test_mutare_locatie import test_mutare_locatie
from Tests.test_pret_maxim_locatie import test_pret_maxim_locatie
from Tests.test_sume_preturi_locatie import test_sume_preturi_locatie
from Tests.test_undo_redo import test_undo_redo
from UserInterface.console import run_ui, show_menu
from UserInterface.console2 import run_ui2


def main():
    while True:
        obiecte = []
        undo_list = []
        redo_list = []
        """obiecte = create(obiecte, 1, 'imprimanta', 'performanta', 800, 'LOC4', undo_list, redo_list)
        obiecte = create(obiecte, 2, 'telefon', 'nou', 700, 'LOC4', undo_list, redo_list)
        obiecte = create(obiecte, 3, 'fax', 'bun', 400, 'LOC5', undo_list, redo_list)
        obiecte = create(obiecte, 4, 'caiet', 'A4', 4, 'LOC2', undo_list, redo_list)
        obiecte = create(obiecte, 5, 'foi', 'A4', 5, 'LOC2', undo_list, redo_list)"""
        print('1. Meniul cu cerinte')
        print('2. Meniul cu consola noua')
        print('x. Exit')
        optiune = input('Alegeti meniul dorit')
        if optiune == '1':
            obiecte = run_ui(obiecte, undo_list, redo_list)
        elif optiune == '2':
            obiecte= run_ui2(obiecte)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    test_crud()
    test_mutare_locatie()
    test_concatenare_string_descriere()
    test_pret_maxim_locatie()
    test_sume_preturi_locatie()
    test_undo_redo()
    main()

