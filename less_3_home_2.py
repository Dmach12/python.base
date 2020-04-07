#1)	Реализовать функцию, принимающую несколько параметров,описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, age, city, email, phone):
    print(f'name - {name}, surname - {surname}, age - {age}, city - {city}, email - {email}, phone - {phone}')
my_func(name='Иван', surname='Иванов', age='40 лет',city= 'Гороховец', email= 'ivanov@mail.ru', phone='+74923822034'  )
