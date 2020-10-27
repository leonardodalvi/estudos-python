lista = [2, 4]

nova_lista = filter(lambda item: item % 2 != 0, lista)
print(list(nova_lista))