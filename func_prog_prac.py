def strip_evens(n):
    return [i * 2 + 1 for i in range(n // 2)]

def flatten(nested_list):
    current_list = []
    def flatten_rec(nested_list):
        print(nested_list)
        current_list.append(nested_list) if not isinstance(nested_list, list) else map(flatten_rec, nested_list)
        # if not isinstance(nested_list, list):
        #     current_list.append(nested_list)
        # else:
        #     for i in nested_list:
        #         flatten_rec(i)
        # return current_list
    return flatten_rec(nested_list)

print(flatten([[1, 2, [3, 4]], [5, 6], 7]))
