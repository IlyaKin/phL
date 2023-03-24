# Задание2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def about_user(name, surname, birth_year, city, email, phone):
    print(f"{name} {surname} {birth_year} {city} {email} {phone}")


about_user(name='Ilya', surname='Kin', birth_year='1991', city='SPB', email='test@mail.com', phone='12345')
