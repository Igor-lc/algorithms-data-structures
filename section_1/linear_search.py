'''ЛИНЕЙНЫЙ ПОИСК. LINEAR SEARCH.
Фактически, этот алгоритм шаг за шагом в цикле перебирает все элементы списка до тех пор пока не найдет искомый или список не закончится.
Actually, this algorithm step by step iterates through all the elements of the list until it finds the desired one or until the list ends.
Рассмотрим ситуацию, когда в массиве из 6 элементов [7, 8, 5, 2, 13, 8] нужно найти элемент со значением 13.
Let's consider a situation where in an array of 6 elements [7, 8, 5, 2, 13, 8], you need to find an element with the value of 13.
На первом шаге алгоритм проверит элемент с нулевым индексом и сравнит его со значением 13.
On the first step, the algorithm will check the element with index zero and compare it to the value of 13. И так до тех пор пока не будет найден нужный элемент.
And so on until the required element is found. После алгоритм вернет его индекс. Afterward, the algorithm will return the index.
Если элемента в массиве нет то цикл дойдет до конца и функция вернет -1 или какое-то другое значение.
If the element is not present in the array, the loop will reach the end, and the function will return -1 or some other value.
В простейшем случае, алгоритм на языке Python выглядит так: In the simplest case, the algorithm in the Python language looks like this:'''

def linear_search(values, target):
    i = 0
    while i < values.__len__():
        if values[i] == target:
            return i
        i += 1
    return -1

print(linear_search([4, 5, 6, 19, 4, 6], 19))
print(linear_search([4, 5, 6, 19, 4, 6], 21))

'''Как я сказал, алгоритм работает с любыми списками, как отсортированными, так и не отсортированными. As I mentioned, the algorithm works with any lists, both sorted and unsorted. 
Если же мы знаем, что список отсортирован, то алгоритм можно усовершенствовать: If, however, we know that the list is sorted, then we can optimize the algorithm:'''

def linear_search(values, target):
    i = 0
    while i < values.__len__():
        if values[i] == target:
            return i
        if values[i] > target:
            return -1
        i += 1
    return -1

print(linear_search([4, 5, 6, 19, 48, 61], 19))
print(linear_search([4, 5, 6, 18, 19, 20], 21))

'''Теперь функция вернет -1 сразу как только цикл пройдет возможную позицию элемента. Now the function will return -1 as soon as the loop passes the potential position of the element. 
Но не забывайте, что это работает только для отсортированных массивов. But remember this only works for sorted arrays. В целом линейный поиск хоть и позволяет работать с любыми списками, 
он гораздо медленнее других алгроритмов поиска, но о них позже, а сейчас рассмотрим простой алгоритм сортировки данных. 
Overall, linear search, while allowing working with any lists, is much slower than other search algorithms. However, there will be separate articles about them. 
Now, let's consider a simple data sorting algorithm.'''

def linear_search(values, value):
    return next((i for i, v in enumerate(values) if v == value), -1)


idx = linear_search([1, 2, 3, 4], 3)
print(idx)