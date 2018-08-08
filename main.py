from collections import namedtuple

Loop = namedtuple('Loop', ['length', 'start_element'])


class Node:
    def __init__(self, value, next = None):
        self.next = next
        self.value = value

    def __str__(self):
        return f'Node({self.value})'

    def __repr__(self):
        return self.__str__()


def build_list_with_loop():
    """
             5 <- 4
             V    ^   
        1 -> 2 -> 3
    """
    _1 = Node(1)
    _1.next = _2 = Node(2)
    _2.next = _3 = Node(3)
    _3.next = _4 = Node(4)
    _4.next = _5 = Node(5)
    _5.next = _2
    return _1


def build_list_without_loop():
    return Node(1, Node(2, Node(3, Node(4, Node(5)))))


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
        current_fist = current_second = start
        for _ in range(loop_length):
            current_fist = current_fist.next
        while current_fist != current_second:
            current_fist = current_fist.next
            current_second = current_second.next
        return current_fist

    element_inside_loop = try_find_element_inside_loop()
    if element_inside_loop:
        loop_length = find_loop_length(element_inside_loop)
        start_element = find_start_element_of_loop(loop_length)
        return Loop(length=loop_length, start_element=start_element)
    else:
        return None

def main():
    list_with_loop = build_list_with_loop()
    list_wihtout_loops = build_list_without_loop()
    print(find_loop(list_with_loop), find_loop(list_wihtout_loops))

if __name__ == '__main__':
    main()