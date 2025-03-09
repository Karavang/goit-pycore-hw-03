from datetime import datetime


def get_days_from_today(date):
    try:
        # Ми повертаємо різницю між сьогоднішньою датою та датою, яка нам прийшла у форматі рядка
        return (datetime.today() - datetime.strptime(date, "%Y-%m-%d")).days
    except ValueError:
        return "Невірний формат заданої дати"


print(get_days_from_today("2028-01-05"))
