from datetime import datetime

def get_days_from_today(date_string):
    # Спочатку перевіряємо, чи взагалі нам передали рядок
    if not isinstance(date_string, str):
        print("Помилка: вхідні дані мають бути рядком (текстом).")
        return None

    try:
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    
    except ValueError:
        # Тут ми детально пояснюємо, що саме пішло не так
        print(f"Помилка: рядок '{date_string}' має неправильний формат.")
        print("Будь ласка, використовуйте РРРР-ММ-ДД (наприклад, 2024-12-31).")
        return None

# ТЕСТУЄМО:
get_days_from_today("12/12/2024") # Неправильний роздільник
get_days_from_today("2024-13-01") # Неіснуючий місяць (13-й)
print(f"Результат для 2020-05-05: {get_days_from_today('2020-05-05')}")

# Вибираємо дату в майбутньому (наприклад, Новий рік 2027)
future_date = "2027-01-01"
result = get_days_from_today(future_date)

print(f"Тест для майбутньої дати ({future_date}):")
print(f"Результат: {result}")





