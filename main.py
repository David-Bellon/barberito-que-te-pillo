import threading
from time import sleep
from random import randint
import names
from collections import deque



class Barbero():
    clientes = deque()
    estado = "Durmiendo"

sem = threading.Semaphore()

def cortarPelo():

    while True:
        if len(Barbero.clientes) == 0:
            print("Sin clientes barbero sopa")
        else:
            
            for i in list(Barbero.clientes):
                sem.acquire()
                Barbero.estado = "Cortando"
                print("Cortando pelo a " + str(i))
                sleep(2)
                print("Termina de cortar pelo")
                Barbero.clientes.popleft()
                sem.release()
                sleep(0.1)
            Barbero.estado = "Durmiendo"
               
            

def addCliente():
    while True:
        sleep(0.5)
        a = randint(0,9)
        if a <= 6:
            if Barbero.estado == "Durmiendo":
                Barbero.clientes.append(names.get_full_name())
                print("Cliente añadido mientras dormia")
                sleep(0.4)
            else:
                if len(Barbero.clientes) >= 7:
                    print("Cola mayor de siete personas, esperando a que uno acabe")
                    print("Cola de clientes: " + str(len(Barbero.clientes)) + "/" + str(7))
                    sem.acquire()
                    Barbero.clientes.append(names.get_full_name())
                    print("Cliente añadido mientras el barbero corta")
                    sem.release()
                    sleep(0.4)
                else:
                    Barbero.clientes.append(names.get_full_name())
                    print("Cliente añadido mientras corta")
                    print("Cola de clientes: " + str(len(Barbero.clientes)) + "/" + str(7))
                    sleep(0.4)

                

barbero = threading.Thread(target=cortarPelo)
clienes = threading.Thread(target=addCliente)

barbero.start()
clienes.start()