def naissance(age):
    an = 2021 - age
    return an

def facorielle(nb):
    if nb == 0:
        return 1
    else:
        e = 1
        while nb > 0:
            e *= nb
            nb = nb + 1
        return e
