ВВЕДЕНИЕ В АЛГОРИТМЫ. INTRODUCTION TO ALGORITHMS.
Умение строить эффективные алгоритмы — один из ключевых навыков современного программиста. The ability to construct efficient algorithms is one of the key skills of a modern programmer. Чтобы понять как работает алгоритм недостаточно просто посмотреть на последовательность шагов, нужно понимать еще несколько его свойств: To understand how an algorithm works, it's not enough to simply look at the sequence of steps you also need to comprehend several of its properties:
1. Скорость. Speed. Быстро он работает или нет, можем ли мы его ускорить, одинакова ли скорость работы на всех входящих данных How fast it operates, whether we can optimize it further, and if its performance remains consistent across different input data?
2. Требование к памяти. Memory requirements. Сколько компьютерных ресурсов нужно алгоритму, является ли такой объем оптимальным, будет ли он работать быстрее если увеличить память? How much computer resources the algorithm needs, whether the amount is optimal, and if it would perform faster if memory is increased?  
3. Правильность. Correctness. Если алгоритм не справляется с поставленной задачей, т.е. выдает не правильное решение то пользы от такого алгоритма нет. If the algorithm fails to accomplish the given task, meaning it produces an incorrect solution, then there is no benefit from such an algorithm.
4. Надежность. Reliability. Хороший алгоритм как правило простой и интуитивно понятный. A good algorithm is typically simple and intuitively understandable. Алгоритм который все время выдаёт различные результаты или срабатывает лишь время от времени является не надёжным, внедрять такие алгоритмы в вашу программу не безопасно. An algorithm that consistently produces different outcomes or only works sporadically is considered unreliable; integrating such algorithms into your program is not safe.
5. Эффективность. Efficiency.  Эффективность — это один из важнейших параметров. Efficiency is one of the most important parameters. Ведь если правильный и надежный алгоритм будет выполняться несколько лет или ему потребуется не доступный объём памяти, то смысла в этом алгоритме нет. If a correct and reliable algorithm runs for several years or requires an impractical amount of memory, then there's no point in using such an algorithm. Поэтому программисты часто задают вопрос: а что будет если увеличить количество входящих данных, не увеличится ли время его выполнения, а если увеличится то на сколько? That's why programmers often ask: what will happen if we increase the amount of input data? Will the execution time stay the same, or will it increase? And if it does increase, by how much? Чтобы понять как сложность задачи влияет на производительность алгоритма, программисты используют понятие «Асимптотическая сложность». To understand how the complexity of a problem affects the performance of an algorithm, programmers use the concept of «Asymptotic Complexity».
