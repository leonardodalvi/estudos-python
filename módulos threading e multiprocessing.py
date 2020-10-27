from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)

if __name__ == '__main__':
    t = Thread(target=funcao_a, args=("Minha Thread",))
    t.start()

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()