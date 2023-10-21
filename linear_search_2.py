def linear_search(values, value):
    idx = [i for i, v in enumerate(values) if v == value]
    return (-1, idx)[idx != []]


def linear_search2(values, value):
    idx = [i for i, v in enumerate(values) if v == value]
    return idx or -(idx == [])

def linear_search3(values, value):
    return [i for i, v in enumerate(values) if v == value] or -1


idx = linear_search([1, 3 ,3 ,4], 5)
print(idx)

idx = linear_search2([1, 3 ,3 ,4], 5)
print(idx)

idx = linear_search3([1, 3 ,3 ,4], 5)
print(idx)