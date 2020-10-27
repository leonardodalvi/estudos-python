lista = [1, 2, 3, 4, 5]

def impar(item):
    return item % 2 != 0

nova_lista = filter(impar, lista)
print(list(nova_lista))