import random


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> List[int]:
    """
    Генерує набір унікальних випадкових чисел для лотерейного білета.
    """
    # Перевірка вхідних параметрів
    if not (1 <= min_val <= max_val <= 1000):
        return []
    
    if not (min_val <= quantity <= (max_val - min_val + 1)):
        return []

    try:
        numbers = random.sample(range(min_val, max_val + 1), quantity)
        numbers.sort()
        return numbers
    except (ValueError, TypeError):
        return []


if __name__ == "__main__":
    # Перевірка використання 
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(f"Ваші лотерейні числа: {lottery_numbers}")



