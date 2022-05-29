# Определить функцию-генератор fib_generator(n), которая принимает количество
# элементов последовательности Фибоначчи и итерируется по элементам
# последовательности.
# например fib_generator(3) создаст итератор для 3 элементов последовательности
# 0 1 1
# Чи́сла Фибона́ччи — элементы числовой последовательности
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
# 4181, 6765, 10946, 17711, …, в которой первые два числа равны 0 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел
# Написать подобную ф-ю fib_list(n) которая возвращает список с элементами
# последовательности.
# Вызов ф-и fib_list(3) вернет список [0, 1, 1]

def fib_generator(n):
    i = 0
    a, b = 0, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


fib_g = fib_generator(15)
print(f'Function-generator Fibonacci {type(fib_g)}:')
for num in fib_generator(15):
    print(num)

seq = []


def fib_list(n):
    i = 0
    a, b = 0, 1
    while i < n:
        yield a
        seq.append(a)
        a, b = b, a + b
        i += 1


fib_l = fib_list(15)
print(f'Function-list Fibonacci {type(fib_l)}:')
for num in fib_list(15):
    print(num)
print(f'List of sequence Fibonacci: {seq}')
