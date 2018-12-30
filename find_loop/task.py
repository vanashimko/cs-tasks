from collections import namedtuple
from shared.node import Node


Loop = namedtuple('Loop', ['length', 'start_element'])


def find_loop(start):
    def try_find_element_inside_loop():
        fast = slow = start
        result = None
        while fast and result is None:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                if fast is slow:
                    result = slow
            else:
                result = False
        return result
    
    def find_loop_length(element_inside_loop):
        current = element_inside_loop.next
        loop_length = 1
        while element_inside_loop != current:
            current = current.next
            loop_length += 1
        return loop_length

    def find_start_element_of_loop(loop_length):
        current_first = current_second = start
        for _ in range(loop_length):
            current_first = current_first.next
        while current_first != current_second:
            current_first = current_first.next
            current_second = current_second.next
        return current_first

    element_inside_loop = try_find_element_inside_loop()
    if element_inside_loop:
        loop_length = find_loop_length(element_inside_loop)
        start_element = find_start_element_of_loop(loop_length)
        return Loop(length=loop_length, start_element=start_element)
    else:
        return None