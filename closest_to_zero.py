def closest_to_zero(lst):
    """
    PT-BR: Busca na lista o valor mais proximo de zero.
    EN: Find the closest number to zero in a python list
    """

    diffs = {value: abs(value - 0) for value in lst}

    return min(diffs, key=diffs.get)


print(closest_to_zero([1, 2, 6, 9, 7, 7, 1]))
