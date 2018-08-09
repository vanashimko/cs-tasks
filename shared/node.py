class Node:
    def __init__(self, value, next = None):
        self.next = next
        self.value = value

    def __str__(self):
        return f'Node({self.value})'

    def __repr__(self):
        return self.__str__()