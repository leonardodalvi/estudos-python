valores = [10, 20, 30]

def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista

print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))