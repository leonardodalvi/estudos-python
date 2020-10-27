from threading import Thread
from multiprocessing import Process, Value

def funcao_a(indice, cont):
    for i in range(100000):
        with cont.get_lock():
            cont.value += 1
    print("Termino processo ", indice)

if __name__ == '__main__':
    contador = Value('i', 0)
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice, contador))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador.value)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador.value)