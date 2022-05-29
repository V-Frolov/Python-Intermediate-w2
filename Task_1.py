# Необходимо написать функцию калькулятор, которая принимает строку состоящую
# из числа, оператора и второго числа разделенных пробелом. Например ('1 + 1');
# Необходимо разделить строку используя str.split(), и проверить является
# результирующий список валидным.
# a) Если ввод не состоит из 3 элементов, необходимо возбудить исключение
# FormulaError, которое является пользовательским исключением.
# b) Попытайтесь сконвертировать первое и третье значение ввода к типу float.
# Перехватите любые исключения типа ValueError, которые возникают, и выбросите
# FormulaError
# c) Если второе значение ввода не является '+', '-', '*', '/' также выбросите
# FormulaError.
# Если инпут валидный - ф-я должна вернуть результат операции

class FormulaError(Exception):
    def __init__(self, message="FormulaError"):
        self.message = message
        super().__init__(self.message)

arr = []

def calc(input_string):
    operators = ['+', '-', '*', '/']
    try:
        for part in input_string.split(' '):
            arr.append(part)
        if (len(arr) == 3) and (arr[1] in operators):
            try:
                arg1 = float(arr[0])
                print('First number:', arg1)
                arg2 = float(arr[2])
                print('Second number:', arg2)
            except ValueError:
                print('Number is not float')
        else: raise FormulaError
    except FormulaError:
        print('Is something wrong. FormulaError')
    else:
        if arr[1] == '+':
            return arg1 + arg2
        elif arr[1] == '-':
            return arg1 - arg2
        elif arr[1] == '*':
            return arg1 * arg2
        elif arr[1] == '/':
            return arg1 / arg2

input_string = input('Enter two float numbers separated by spaces and a math operator: ')
result = calc(" ".join(input_string.split()))
print(f'Result of {arr[1]}: {result}')