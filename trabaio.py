from typing import List, Any

class Queue:
    
    def __init__(self, valor_max = None) -> None:
	"""Inicializa uma fila vazia. valor_max define o limite (None para ilimitada)."""
        self.__data: List[Any] = []
        self.__valor_max = valor_max
        
    def enqueue(self, ele: Any) -> None:
	"""Adiciona um item ao final da fila. Lança OverflowError se estiver cheia."""
        if self.__valor_max != None and len(self.__data) >= self.__valor_max:
            raise Exception("OverflowError")
            
        self.__data.append(ele)

    def dequeue(self) -> Any:
	"""Remove e retorna o primeiro item da fila. Lança IndexError se estiver vazia."""
        if (len(self.__data) == 0):
            raise Exception("IndexError")
        return self.__data.pop(0)
        
    def peek(self) -> Any:
	"""Retorna o primeiro item da fila sem removê-lo. Lança IndexError se estiver vazia."""
        if (len(self.__data) == 0):
            raise Exception("IndexError")
        return self.__data[0]
    
    def is_empty(self) -> bool:
	"""Retorna True se a fila estiver vazia, False caso contrário."""
        return len(self.__data) == 0
    
    def is_full(self) -> bool:
	"""Retorna True se a fila atingiu o valor_max, False caso contrário."""
        return self.__valor_max != None and len(self.__data) >= self.__valor_max
    
    def size(self) -> int:
	"""Retorna a quantidade atual de elementos na fila."""
        return len(self.__data)
    
    def clear(self) -> None:
	"""Remove todos os elementos da fila."""
        self.__data.clear()
        
    def __repr__(self) -> str:
	"""Retorna uma representação em string da fila."""
        return str(self.__data)

print("Teste 1: Criando a fila e adicionando numeros")
fila = Queue()
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
print(fila)

print("Teste 2: Verificando o tamanho da fila")
print(fila.size())

print("Teste 3: Espiando o primeiro numero da fila")
print(fila.peek())

print("Teste 4: Removendo o primeiro numero")
print(fila.dequeue())
print(fila)

print("Teste 5: Esvaziando a fila de vez")
fila.clear()
print(fila)	