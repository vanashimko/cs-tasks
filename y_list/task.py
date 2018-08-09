from shared.node import Node

def find_vanishing_point(start_first, start_second):
    def find_length(start):
        length = 0
        current = start
        while current:
            current = current.next
            length += 1
        return length
    
    first_length = find_length(start_first)
    second_length = find_length(start_second)

    current_first = start_first
    current_second =  start_second
    
    while second_length > first_length :
        current_second = current_second.next
        second_length -= 1
    while first_length > second_length:
        current_first  = current_first.next
        first_length -= 1

    while current_first != current_second:
        current_first = current_first.next
        current_second = current_second.next

    return current_first

