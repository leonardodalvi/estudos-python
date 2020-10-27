escolha = input("Escolha uma opção de função: 1 ou 2")
if escolha == 1:
    def func1(x):
        return x + 1
else:
    def func2(x):
        return x + 2

s = func1(10)
print(s)
