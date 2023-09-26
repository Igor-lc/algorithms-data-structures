'''СЛОЖНЫЕ ПРОЦЕНТЫ. COMPOUND INTEREST.
Сложный процент — это такой эффект, когда начисленные проценты по вкладу прибавляются к общей сумме вклада и в дальнейшем сами участвуют в создании дополнительного дохода.
Compound interest is an effect where the accrued interest on a deposit is added to the total deposit amount, and subsequently, it itself contributes to generating additional income.
Давайте посмотрим на функцию вычисления сложных процентов. Let's take a look at the function for calculating compound interest:'''

def compound(amount, year_percent, months):
    months_percent = year_percent / 12
    for i in range(months):
        inc = amount / 100 * months_percent
        amount += inc
    return amount

print(compound(100000, 10, 12))

'''Функция принимает 3 аргумента: начальный вклад, годовой процент и продолжительность вклада в месяцах. The function takes 3 arguments: initial deposit, annual interest rate, 
and the duration of the deposit in months.	 Сперва мы вычисляем ежемесячный процент а затем запускаем цикл, в котором расчитываем ежемесячную начисленную сумму и добавляем эту сумму ко вкладу.
 First, we calculate the monthly interest rate, and then we enter a loop where we compute the monthly accrued amount and add this amount to the deposit. 
 В конце функция возвращает итоговое значение. At the end, the function returns the final value. Все довольно просто. Если передать в программу compound(100000, 10, 12) то получим 110471. 
 If you input compound(100000, 10, 12) into the program, you will get 110471.
Однако это не оптимальный вариант расчета сложный процентов. However, this is not the most optimal way to calculate compound interest. Мы используем цикл и чем дольше будет срок – 
тем больше вычислений будет произведено. We are using a loop, and the longer the duration, the more calculations will be performed. При расчете полугодового вклада цикл сделает всего 6 итераций, 
а для пятилетнего вклада потребуется 60. When calculating a semi-annual deposit, the loop will perform only 6 iterations, while for a five-year deposit, it will require 60 iterations. 
Однако есть альтернативное решение в 1 действие. However, there is an alternative solution that requires just one calculation. Расчет можно сделать с помощью специальной формулы, вместо цикла. 
The calculation can be done using a specific formula instead of a loop:'''
def compound(amount, year_percent, months):
    months_percent = year_percent / 12
    return amount * (1 + months_percent / 100) ** months
print(compound(100000, 10, 12))

'''Как видите задачу мы решаем одну, а алгоритмы используем разные. As you can see, we are solving the same problem, but using different algorithms. 
При этом рассмотренные алгоритмы имеют имеют различную вычислительную сложность. Moreover, the discussed algorithms have different computational complexities. 
Но о том как считать эффективность алгоритмов позже, а следующим рассмотрим классический алгоритм линейного поиска, который позволяет найти элемент в любом списке, как отсортированном, так и нет. 
But discussing how to measure algorithm efficiency is for later. 
Next, let's consider the classic linear search algorithm, which allows us to find an element in any list, whether it's sorted or not.'''