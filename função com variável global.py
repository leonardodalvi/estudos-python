def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')
