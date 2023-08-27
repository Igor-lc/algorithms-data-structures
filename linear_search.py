def linear_search(values, target):
    i = 0
    while i < values.__len__():
        if values[i] == target:
            return i
        if values[i] > target:
            return -1
        i += 1
    return -1

print(linear_search([4, 5, 6, 19, 4, 6], 19))
print(linear_search([4, 5, 6, 19, 4, 6], 21))