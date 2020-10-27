from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []

def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("Termino processo ", indice)


if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", len(minha_lista))