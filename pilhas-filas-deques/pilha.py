import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)
    
    