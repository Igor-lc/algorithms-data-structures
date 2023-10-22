'''СОРТИРОВКА ВЫБОРОМ. SELECTION SORT.
Сортировка данных — одна из важнейших алгоритмических задач постольку, поскольку алгоритмы поиска лучше работают с отсортированными массивами данными.
Data sorting is one of the most crucial algorithmic tasks, as search algorithms perform better with sorted arrays of data. Рассмотрим простой, но не самый эффективный алгоритм сортировки,
сортировку выбором. Let's consider a simple but not the most efficient sorting algorithm — selection sort. Её суть состоит в том, чтобы найти в списке наибольший элемент и добавить его
в конец отсортированного списка. Its essence is to find the largest element in the list and add it to the end of the sorted list. Или наоборот, найти наименьший и добавить его в начало.
Or conversely, find the smallest element and add it to the beginning. Перед вами список из 6 элементов: [7, 8, 2, 5, 3, 6]. Here is a list of 6 elements in front of you: [7, 8, 2, 5, 3, 6].
На первом шаге алгоритм проходит по всему списку и находит минимальный элемент, 2. In the first step, the algorithm goes through the entire list and finds the minimum element, which is 2.
Далее этот элемент обменивается с тем, с которого начинался поиск, то есть с 7. Then this element is swapped with the one where the search started, which is 7.
После этого получается, что в начале списка стоит самый маленький элемент, а значит далее нужно проделать те же действия с остальной частью списка.
After this, it turns out that the smallest element is at the beginning of the list, which means the same actions need to be performed with the rest of the list.
И продолжаем операцию пока не дойдем до конца списка, после чего все элементы будут отсортированы. And we continue the operation until we reach the end of the list, after which all elements will be sorted.
Посмотрим на код алгоритма на языке Python: Let's take a look at the algorithm code in the Python language:'''

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

'''В коде 2 цикла. There are 2 loops in the code. Внешний перебирает все элементы списка. The outer one iterates through all the elements in the list. И на каждой его итерации запускается 
внутренний цикл, который проходит по оставшимся элементам. And on each of its iterations, the inner loop is launched, which goes through the remaining elements. 
Во внутреннем цикле мы ищем минимальное значение с помощью сравнений. In the inner loop, we search for the minimum value using comparisons. И затем по выходу, снова во внешнем цикле, 
меняем найденные минимальные элементы с первыми значениями. And then on exit, back in the outer loop, we swap the found minimum elements with the initial values. 
Если массив изначально будет отсортирован, то алгоритм всё-равно сделает все замены. If the array is already sorted, the algorithm still performs all the replacements. 
Поэтому мы можем внести в алгоритм дополнение: if i != min_idx, то есть раскоментировать код. So, we can add an addition to the algorithm: if i != min_idx, which means uncommenting the code. 
Теперь лишний замен нет, только проверки на равенства. Now, unnecessary replacements are absent, only equality checks. Обычно проверка на равенство занимает меньше времени, чем замена или 
присваивание. Usually, an equality check takes less time than replacement or assignment. Однако, если массив не отсортирован, то количество замен будет совпадать с количеством проверок и 
такая операция может даже сделать алгоритм медленнее. However, if the array is not sorted, the number of replacements will match the number of checks, and such an operation might even slow 
down the algorithm. Если же мы знаем, что массив частично отсортирован, то такая оптимизация будет полезной. If we know that the array is partially sorted, such an optimization will be beneficial. 
То есть даже такое небольшое изменение в алгоритме может оказать как положительный, так и отрицательный эффект, в зависимости от начальных данных. 
Thus, even such a small change in the algorithm can have both positive and negative effects, depending on the initial data. И при разработке это надо учитывать. During development, this is 
worth considering. В целом сортировка выбором является достаточно быстрой до 10000 элементов. In general, selection sort is quite fast for up to 10000 elements. А для списков до 10 элементов 
она даже часто эффективнее, чем более сложные алгоритмы. And for lists of up to 10 elements, it's often even more effective than more complex algorithms.'''