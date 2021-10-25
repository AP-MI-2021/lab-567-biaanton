from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    obiecte= []
    obiecte = create(obiecte, 1, 'imprimanta', 'performanta', 800, 'C4')
    obiecte=run_ui(obiecte)

if __name__ == '__main__':
    test_crud()
    main()

