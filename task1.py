from datetime import datetime

def get_days_from_today(date_string):
    """
    Розраховує кількість днів між заданою датою та поточною датою.
    
    Параметр:
    date_string (str): Дата у форматі 'YYYY-MM-DD'.
    
    Повертає:
    int: Кількість днів. Позитивне — дата в минулому, негативне — в майбутньому.
    """
    if not isinstance(date_string, str):
        print("Помилка: вхідні дані мають бути рядком.")
        return None

    try:
        # Перетворення рядка у об'єкт date
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        # Отримання поточної дати без часу
        today = datetime.today().date()
        # Повернення різниці у днях
        return (today - given_date).days
    
    except ValueError:
        print(f"Помилка: '{date_string}' не відповідає формату РРРР-ММ-ДД.")
        return None

# Приклади використання
if __name__ == "__main__":
    # Тест із завдання
    print(f"Результат для 2020-10-09: {get_days_from_today('2020-10-09')}")
    
    # Тест майбутньої дати
    print(f"Результат для 2027-01-01: {get_days_from_today('2027-01-01')}")
    
    # Тест на помилку
    get_days_from_today("неправильна-дата")





