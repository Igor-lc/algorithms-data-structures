'''СЛОЖНОСТЬ АЛГОРИТМОВ. ALGORITHMS COMPLEXITY.
Сложность алгоритма — это информация о том, на сколько он быстро работает. Algorithm complexity is information about how quickly it operates. Причем измерение скорости не затрагивает какие-то
особенности языка программирования или мощность компьютера. Moreover, measuring speed doesn't involve specific programming language features or computer power. Это оценка именно алгоритма в чистом
виде. It's an evaluation of the algorithm itself in its pure form.

1000 users —> Algorithm O(n) —> 5 seconds

Анализ сложности также позволяет спрогнозировать как поведет себя алгоритм при возрастании потока входящих данных. Complexity analysis also allows predicting how the algorithm will behave as the
incoming data volume increases. На практике такие оценки очень важны. In practice, such assessments are very important. Ведь если мы написали алгоритм для сайта, который обслуживает 1000
посетителей и измерили его время выполнения, то с помощью анализа сложности мы сможем довольно точно спрогнозировать что случится, если число пользователей возрастет до 2000 или до 10 000.
For instance, if we've developed an algorithm for a website serving 1000 visitors and measured its execution time, with the help of complexity analysis, we can quite accurately predict what will
happen if the user count increases to 2000 or 10,000. Для обозначения сложности или производительность алгоритмов используется нотация большое О. To denote the complexity or performance of
algorithms, the "Big O" notation is used. О(n2) означает что при увеличении количества входящих данных время работы алгоритма или объем памяти возрастет квадратично. O(n^2) means that as the
amount of input data increases, the algorithm's runtime or memory usage will grow quadratically.
Давайте вычислим сложность 3 алгоритмов описанных выше. Let's calculate the complexity of the three algorithms described above. Начнем из алгоритма для вычисления сложных процентов из циклом и
из формулой. We'll start with the algorithm for calculating compound interest using a loop and a formula.'''

def compound(amount, year_percent, months):
    months_percent = year_percent / 12	    	# (2)
    for i in range(months):				        # (1)(1)
        inc = amount / 100 * months_percent	    # (3)
        amount += inc				            # (1)
    return amount

'''Сперва определимся с фундаментальными инструкциями, то есть такими инструкциями, которые выполняются процессором мгновенно. First, let's start with the fundamental instructions, that is, 
instructions that are executed by the processor instantly. Это присваивание, сравнение, основные арифметические операции и так далее. These include assignment, comparison, basic arithmetic 
operations, and so on. Для 1 строки требуется 2 инструкции: деление и присваивание. It takes 2 instructions for 1 line: division and assignment. Причем эти 2 инструкции требуются алгоритму 
всегда, независимо от количества месяцев депозита. Moreover, these 2 instructions are always required by the algorithm, regardless of the number of months in the deposit. Далее идет цикл for 
котором будет 1 операция — инициализация итератора range(). Next comes a 'for' loop in which there will be 1 operation - the initialization of the range() iterator. Все это происходит еще до 
1 запуска цикла. All of this happens even before the first loop iteration. В начале каждой итерации мы будем иметь еще 1 операцию — увеличение счетчика i  на 1. At the beginning of each 
iteration, we will have one more operation - incrementing the counter i by 1. В 1 строке цикла происходит 3 операции: деление, умножение и присваивание, а во второй строке — 1 операция, 
инкремент. In the first line of the loop, 3 operations occur: division, multiplication, and assignment. In the second line, there is 1 operation — an increment. Таким образом мы получаем 
следующее количество инструкций: (2 + 1) = 3 на инициализацию алгоритма и (1 + 3 + 1) = 5 на каждую итерацию. Thus, we get the following number of instructions: (2 + 1) = 3 for the algorithm 
initialization, and (1 + 3 + 1) = 5 for each iteration. При этом количество итераций зависит от количества месяцев. The number of iterations, in turn, depends on the number of months. 
Теперь мы можем определить математическую функцию, описывающую наш алгоритм. Now we can define the mathematical function describing our algorithm:
f(n) = 3 + 5n, где n – это количество итераций, where n is the number of iterations.
Однако на практике нет необходимости подсчитывать каждую отдельную операцию в программе. However, in practice, there's no need to count each individual operation in the program. 
И зачастую такие функции очищают от незначительных деталей. And often, such functions are cleaned from insignificant details. В нашем случае важно лишь то, что будет происходить с функцией 
при значительном увеличении n. In our case, it's important only what will happen to the function with a significant increase in n. Поэтому мы легко можем отбросить те элементы, которые растут 
медленно и тогда останется f(n) = 5n. Therefore, we can easily discard elements that grow slowly, and then we'll be left with f(n) = 5n. Далее, на что можно не обращать внимание, так это на 
множитель перед n. Next, something we can ignore is the coefficient in front of n. То есть наша функция превращается просто в f(n) = n. In other words, our function simply becomes f(n) = n. 
Фактически нет особой разницы, какое количество операций, 5 или 10 выполняется внутри цикла. In fact, there isn't much difference in the number of operations, 5 or 10, being executed inside 
the loop. Важно только количество повторений этих операций. What matters is only the number of repetitions of these operations. К тому же мы исследуем алгоритм в чистом виде и при переносе его 
на разные языки, скорость операций внутри цикла может значительно отличаться. Moreover, as we examine the algorithm in its pure form, the speed of operations inside the loop can significantly 
vary when it's translated into different languages. Как я уже говорил, для обозначения сложности алгоритмов обычно используют O нотации. As I already mentioned, to denote algorithm complexity, 
"O" notation is commonly used. И для нашего алгоритма это будет О(n) – линейная сложность. And for our algorithm, that will be O(n) – linear complexity. Для многих алгоритмов линейная сложность 
считается очень хорошей. For many algorithms, linear complexity is considered very favorable.
Теперь рассмотрим второй алгоритм. Now let's consider the second algorithm:'''

def compound(amount, year_percent, months):
    months_percent = year_percent / 12			           # (2)
    return amount * (1 + months_percent / 100) ** months   # (4)

'''В нем 2 строки и 1-я как мы выяснили состоит из 2 операций, а 2-я из 4. It has 2 lines, and first, as we determined, consists of 2 operations, while the other has 4. Итого f(n) = 6. 
In total, f(n) = 6. В данном случае 6 мы совсем не отбрасываем, а приводим к 1, f(n) = 1, чтобы показать, что функция не равна нулю. In this case, we reduce 6 to 1; we keep it as f(n) = 1 to 
show that the function is not equal to zero. Итого сложность второго алгоритма равна О(1) – константная сложность. Hence, the complexity of the second algorithm is O(1) – constant complexity. 
Что означает, что алгоритм всегда будет выполнятся за один и тот же отрезок времени. Не зависимо от сложности задачи. This means that the algorithm will always execute within the same timeframe, 
regardless of the problem's complexity. Теперь он не зависит от количества месяцев. Now it doesn't depend on the number of months. Однако это не значит, что он обязан выполняться быстро. 
However, this doesn't mean that it must execute quickly. О(1) алгоритмы могут быть и долгими, однако на каком бы наборе данных мы их не запускали, они всегда будут выполнятся за константное время. 
O(1) algorithms can also be time-consuming. Nevertheless, no matter what dataset we run them on, they will always run in constant time. В нашем же случае очевидно, что О(1) эффективнее О(n). 
In our case, it's evident that O(1) is more efficient than O(n). По этому его и нужно использовать. That's why it should be used.
Теперь проанализируем код алгоритма линейного поиска. Now let's analyze the code of the linear search algorithm. Рассмотрим два набора данных. Let's consider two sets of data:
[1, 3, 5, 7, 9, 11]
[11, 1, 3, 7, 9, 5]
В обоих случаях нам нужно найти число 11. In both cases, we need to find the number 11. Очевидно, что в 1 случае цикл пройдет по всем элементам, так как искомое значение находится в конце. 
It is evident that in the first scenario, the loop will traverse through all the elements since the desired value is located at the end. То есть будет произведено n итераций, где n – это длина 
списка. Thus, n iterations will be performed, where n is the length of the list. Во втором случае будет выполнена всего 1 итерация, так как искомое значение стоит в самом начале. 
In the second case, only 1 iteration will be executed, as the sought value is at the very beginning. Если бы мы опирались на фактические данные, то в 1 случае сложность алгоритма была бы О(n), 
а во 2 О(1), то есть разница в скорости работы алгоритма между 2 наборами данных — существенна. If we relied on actual data, the complexity of the algorithm in the first case would be O(n), 
while in the second case, it would be O(1), signifying a significant difference in the algorithm's speed between the two data sets. Но на практике при анализе мы исследуем не фактические данные, 
а оцениваем сам алгоритм, поэтому нужно всегда исходить из наиболее не благоприятного случая. То есть есть смысл рассматривать только 1 вариант. However, in practice, during analysis, 
we explore not actual data but rather assess the algorithm itself. Hence, we must always consider the worst-case scenario, meaning we should focus on the first scenario. 
А значит сложность алгоритма линейного поиска О(n). Consequently, the complexity of the linear search algorithm is O(n). При этом мы учитываем, что при определенных наборах данных алгоритм 
отработает гораздо быстрее. While doing so, we take into account that the algorithm will perform much faster under certain data sets. Поэтому есть смысл утверждать, что алгоритм работает или 
плохо как О(n), или, скорее всего — лучше.  Therefore, it makes sense to assert that the algorithm performs poorly in terms of O(n) or, most likely, better. То есть, наш алгоритм асимтотически 
не хуже, чем О(n). In other words, our algorithm is asymptotically no worse than O(n). Существует и более математический способ определения сложности этого алгоритма. There is a more mathematical 
way to determine the complexity of this algorithm. Будем исходить из того, что все элементы в списке расположены в случайном порядке и искомое значение может с равной вероятностью находится в 
любом месте. То есть в вероятностью 1/n. Let's assume that all elements in the list are randomly ordered, and the sought value could be in any position with an equal probability of 1/n. 
При этом если элемент будет на 1 итерации, то цикл выполнится (1 х 1/n) раз. If the element happens to be at the 1st iteration, the loop will execute (1 x 1/n) times. А если он будет стоять в 
конце или искомого элемента вообще не будет, то цикл, то цикл выполнится (n x 1/n) раз. If it's at the end or missing entirely, the loop will execute (n x 1/n) times. В итоге, мы получаем 
следующее среднее время поиска для всех элементов: (1+2+ … +n) / n = (n+1) / 2. То есть успешный поиск методом перебора в среднем занимает O((n+1) / 2) = O(n) – с учетом всех упрощений. 
Ultimately, we obtain the following average search time for all elements: (1+2+ … +n) / n = (n+1) / 2. This implies that successful brute-force search on average takes O((n+1) / 2) = O(n) – 
considering all simplifications. Вообще на практике такие расчеты обычно не делаются. In practice, such calculations are generally not performed.  Программисты исходят из того, что одиночный 
цикл имеет сложность O(n). В большинстве случаев этого достаточно. Но это если циклы стоят рядом. Programmers typically assume that a single loop has a complexity of O(n), which is sufficient 
for most cases. При этом если в алгоритме друг за другом стоят 2 цикла, то сложность так же считается как O(n). Если же циклы вложены друг в друга, то сложность алгоритма с учетом всех упрощений 
увеличивается квадратично. If loops are nested within each other, the algorithm's complexity, with all simplifications considered, increases quadratically. То есть вложенные циклы имеют 
квадратичную сложность — О(n2). Thus, nested loops have quadratic complexity — O(n2).

Кроме О(1) – константной, О(n) – линейной и О(n2) – квадратичной сложностей существуют и другие, но о них позже, в соответствующих алгоритмах.
Apart from O(1) – constant complexity, O(n) – linear complexity, and O(n2) – quadratic complexity, there are other complexities, but we will discuss them later in the corresponding algorithms.'''