from datetime import datetime, timedelta
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


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, перевіряємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження у наступні 7 днів
        if 0 <= (birthday_this_year - today).days <= 7:
            congrats_date = birthday_this_year
            # Якщо день народження випадає на вихідний, переносимо на понеділок
            if congrats_date.weekday() in (5, 6):
                congrats_date += timedelta(days=(7 - congrats_date.weekday()))

            upcoming_birthdays.append(
                {
                    "name": name,
                    "congratulation_date": congrats_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays
