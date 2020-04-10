from sys import argv

salary, output, rate, bonus = argv

output = int(output)
rate = int(rate)
bonus = int(bonus)
salary = output * rate + bonus
print(f'Заработная плата сотрудника {salary}')
