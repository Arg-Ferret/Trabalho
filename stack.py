from typing import Any, List

class Stack:

    def _init_(self) -> None:
        self.__data: List[Any] = []
    
    def push(self, item: Any) -> None:
        self.__data.append(item)
    
    def _repr_(self) -> str:
        return str(self.__data)

    def pop(self) -> Any:
        if not self.__data:
            return None
        return self.__data.pop()
    
    def is_empty(self) -> bool:
        return len(self.__data) == 0
    
    def size(self) -> int:
        return len(self.__data)
    
    def peek(self) -> Any:
        if not self.__data:
            return None
        return self.__data[0]
    
    def invert_list(self):
        data = []
        copy = self.__data.copy()
        for _ in range(len(self.__data)):
            data.append(copy.pop())
        return data