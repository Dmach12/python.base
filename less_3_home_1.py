#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))


def dev (num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return "На ноль делить нельзя"

print(dev(num1, num2))

