#5)	Запросите у пользователя значения выручки и издержек фирмы.Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек,или убыток — издержки больше
# выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
income = int(input('Введите доход фирмы: '))
costs = int(input('Введите издежки фирмы: '))
outcome = income - costs
profit = outcome / income
print(f'Финансовый результат фирмы {outcome}')
if outcome > 0:
    print(f'рентабельность выручки: {profit}')

staff = int(input('Введите численность сторудников: '))
profit_employee = outcome / staff
print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_employee}')



