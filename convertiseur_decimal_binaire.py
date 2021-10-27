def conversion():
    base = int(input("Entrez la base: "))
    x = input("Entrez le nombre à convertir: ")

    if (base != 2 and 16 and 10):
        return print('La base ne corespond pas')
    for i in list(x):
        if int(i) >= base:
            return ("Les nombre ne correspond pas à la base")
    return int(x, base)

#print(conversion())

def decimal_binaire_hex():
    c = int(input('Entrez un nombre: '))
    return (bin(c)), (hex(c))
#print(decimal_binaire_hex())