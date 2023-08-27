def selection_sort(values):
    for i in range(len(values) - 1):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[min_idx] > values[j]:
                min_idx = j

        # if i != min_idx:
        #     values[i], values[min_idx] =  values[min_idx], values[i]
        values[i], values[min_idx] = values[min_idx], values[i]


data = [7, 8, 2, 5, 3, 6, 1, 9]
print("start", data)
selection_sort(data)
print("end", data)