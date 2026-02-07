import random

def get_numbers_ticket(min_val, max_val, quantity): 
    """
    Генерує набір унікальних випадкових чисел для лотерейного білета.
    """
    
    # Перевірка вхідних параметрів
    if not (1 <= min_val <= max_val <= 1000):
        return []
    
    # Додаткова перевірка: чи достатньо чисел у діапазоні для вибору quantity
    if not (min_val <= quantity <= (max_val - min_val + 1)):
        return []

    try:
        # Генерація унікальних випадкових чисел
        numbers = random.sample(range(min_val, max_val + 1), quantity)
        
        # Сортування списку
        numbers.sort()
        
        return numbers
    except (ValueError, TypeError):
        # Обов'язковий блок except для конструкції try
        return []

# Перевірка використання 
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")



