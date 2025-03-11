from datetime import datetime
from random import randint
import re


def get_days_from_today(date):
    try:
        # Ми повертаємо різницю між сьогоднішньою датою та датою, яка нам прийшла у форматі рядка
        return (datetime.today() - datetime.strptime(date, "%Y-%m-%d")).days
    except ValueError:
        return "Невірний формат заданої дати"


def get_numbers_ticket(min, max, quantity):
    # Створюємо множину для того, щоб не було повторень
    arr = set()
    # Робимо перевірку на можливість вибору такої кількості чисел
    if quantity > max - min:
        return []
    # Якщо все круто - генеруємо числа та віддаємо їх у вигляді списку
    while len(arr) != quantity:
        arr.add(randint(min, max))
    return list(arr)


def normalize_phone(phone_number):
    number = ""
    pattern = r"\d+"
    matches = re.findall(pattern, phone_number)
    print(str(matches))
    for match in matches:
        number += match
    if phone_number[0] == "+" or phone_number[0:3] == "380":
        number = "+" + number
    else:
        number = "+38" + number
    return number


print(normalize_phone("380 67 777 77 aboba77"))
