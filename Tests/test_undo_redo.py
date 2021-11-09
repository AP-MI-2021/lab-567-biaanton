from Domain.obiect2 import creeaza_obiect
from Logic.crud import read, delete, create
from Logic.undo_redo import do_undo, do_redo


def get_data():
    return [creeaza_obiect(1, 'o1', 'desc1', 100, 'LOC1'),
            creeaza_obiect(2, 'o2', 'desc2', 60, 'LOC1'),
            creeaza_obiect(3, 'o3', 'desc3', 10, 'LOC3'),
            creeaza_obiect(4, 'o4', 'desc4', 145421, 'LOC4'),
            creeaza_obiect(5, 'o5', 'desc5', 20.87, 'LOC4')
            ]


def test_undo_redo():
        obiecte = []
        undo_list = []
        redo_list = []
        obiecte = create(obiecte, 1, 'o1', 'desc1', 100, 'LOC1', undo_list, redo_list)
        obiecte = create(obiecte, 2, 'o2', 'desc2', 60, 'LOC1', undo_list, redo_list)
        obiecte = create(obiecte, 3, 'o3', 'desc3', 10, 'LOC3', undo_list, redo_list)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 1
        obiecte = do_undo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 0
        obiecte = create(obiecte, 1, 'o1', 'desc1', 100, 'LOC1', undo_list, redo_list)
        obiecte = create(obiecte, 2, 'o2', 'desc2', 60, 'LOC1', undo_list, redo_list)
        obiecte = create(obiecte, 3, 'o3', 'desc3', 10, 'LOC3', undo_list, redo_list)
        obiecte = do_redo(undo_list, redo_list, obiecte)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 1
        obiecte = do_redo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 2
        obiecte = do_redo(undo_list, redo_list, obiecte)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 1
        obiecte = create(obiecte, 4, 'o4', 'desc4', 145421, 'LOC4' , undo_list, redo_list)
        obiecte = do_redo(undo_list, redo_list, obiecte)
        obiecte = do_undo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 1
        obiecte = do_undo(undo_list, redo_list, obiecte)
        assert len(obiecte) == 0
        obiecte = do_redo(undo_list, redo_list, obiecte)
        obiecte = do_redo(undo_list, redo_list, obiecte)





















