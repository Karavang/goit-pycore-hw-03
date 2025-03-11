from datetime import datetime
from random import randint


def get_days_from_today(date):
    try:
        # Ми повертаємо різницю між сьогоднішньою датою та датою, яка нам прийшла у форматі рядка
        return (datetime.today() - datetime.strptime(date, "%Y-%m-%d")).days
    except ValueError:
        return "Невірний формат заданої дати"


def get_numbers_ticket(min, max, quantity):
    arr = set()
    if quantity > max - min:
        return []
    while len(arr) != quantity:
        arr.add(randint(min, max))
    return list(arr)
