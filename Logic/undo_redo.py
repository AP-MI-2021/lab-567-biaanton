def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Sterge ultima operatiune facuta
    :param undo_list: lista dupa stergere
    :param redo_list: lista dinaintea stergerii
    :param current_list: lista curenta
    :return: lista dupa ce a avut loc undo
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Revine la operatiunea dinaintea stergerii
    :param undo_list: lista dupa stergere
    :param redo_list: lista dinaintea stergerii
    :param current_list: lista curenta
    :return:
    """
    if redo_list:
        undo_list.append(current_list)
        return redo_list.pop()
    else:
        return None
