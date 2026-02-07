from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    """
    Повертає список користувачів, у яких день народження наступає протягом наступних 7 днів.
    
    """
    upcoming_birthdays = []
    # Отримуємо поточну дату та дату через 7 днів
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    for user in users:
        # Конвертуємо рядок дати народження в об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначаємо день народження в цьому році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Рахуємо різницю в днях між сьогодні і днем народження
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження протягом наступних 7 днів (включаючи сьогодні)
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Перевіряємо, чи випадає день на вихідний
            day_of_week = congratulation_date.weekday()
            
            if day_of_week == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif day_of_week == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # Додаємо результат у список у потрібному форматі
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.12"}
]
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))

