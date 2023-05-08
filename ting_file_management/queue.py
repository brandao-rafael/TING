from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.linked_list import LinkedList


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = LinkedList()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__data)

    def __str__(self):
        return f"Node(len={len(self.__data)}, value={self.__data})"

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.__data.insert_last(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self.__data) == 0:
            return None
        return self.__data.remove_first().value

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self.__data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__data.get_element_at(index).value
