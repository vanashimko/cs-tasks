def find_symmetry_point(list):
    list_len = len(list)
    right_to_left = [0]
    for i in range(1, list_len):
        right_to_left.append(right_to_left[i - 1] + list[list_len - i])
    result = None
    left_to_right_sum = 0
    for i in range(list_len):
        if left_to_right_sum != right_to_left[list_len - i - 1]:
            left_to_right_sum = left_to_right_sum + list[i]
        else:
            result = i
            break
    return result
