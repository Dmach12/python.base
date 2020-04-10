def wages():
    output = int(input("Введите выработку в часах: "))
    rate = int(input("Введите ставку в час: "))
    bonus = int(input("Введите размер премии: "))
    salary = output * rate + bonus
    print(f'Заработная плата сотрудника {salary}')
wages()
