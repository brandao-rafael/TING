from ting_file_management.node import Node


# classe feita no exercicio
class LinkedList:
    def __init__(self):
        self.head_value = None
        self.tail_value = None
        self.__length = 0

    def __str__(self):
        return f"LinkedList(len={self.__length}, value={self.head_value})"

    def __len__(self):
        return self.__length

    def insert_first(self, value):  # complexity = O(1)
        first_value = Node(value)
        first_value.next = self.head_value

        if self.is_empty():
            self.tail_value = first_value

        self.head_value = first_value
        self.__length += 1

    def insert_last(self, value):  # complexity = O(1)
        last_value = Node(value)

        if self.is_empty():
            return self.insert_first(value)

        self.tail_value.next = last_value
        self.tail_value = last_value
        self.__length += 1

    def insert_at(self, value, position):  # complexity = O(n)
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self.__get_node_at(position - 1)
        next_value = Node(value)
        next_value.next = current_value.next
        current_value.next = next_value
        self.__length += 1

    def remove_first(self):  # complexity = O(1)
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def remove_last(self):  # complexity = O(n)
        if len(self) <= 1:
            return self.remove_first()

        previous_to_be_removed = self.__get_node_at(len(self) - 2)

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = None
        self.__length -= 1
        return value_to_be_removed

    def remove_at(self, position):  # complexity = O(n)
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.__get_node_at(position - 1)

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None
        self.__length -= 1

        return value_to_be_removed

    def get_element_at(self, position):  # complexity = O(n)
        value_returned = None
        value_to_be_returned = self.__get_node_at(position)
        if value_to_be_returned:
            value_returned = Node(value_to_be_returned.value)
        return value_returned

    def is_empty(self):
        return not self.__length

    def clear(self):  # complexity = O(n)
        while not self.is_empty():
            self.remove_first()

    def __get_node_at(self, position):  # complexity = O(n)
        value_to_be_returned = self.head_value
        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
        return value_to_be_returned

    def index_of(self, value):  # complexity = O (n)
        index = 0
        current_value = self.head_value
        while current_value:
            if current_value.value == value:
                return index + 1
            current_value = current_value.next
            index += 1
        return -1
