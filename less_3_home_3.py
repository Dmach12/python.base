#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
def my_func(num1, num2, num3):
    if num1 > num3 and num2 > num3:
        return num1 + num2
    elif num1 > num2 and num3 > num2:
        return num1 + num3
    else:
        return num2 + num3
print(f'Сумма наибольших двух аргументов - {my_func(num1, num2, num3)}')