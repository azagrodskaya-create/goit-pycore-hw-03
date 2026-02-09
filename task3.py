import re


def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону, залишає тількт цифри та + , додає міжнародний код +38, якщо необхідно.
    """
    # Видаляємо всі символи, крім цифр та знаку +
    sanitized_number = re.sub(r"[^\d+]", "", phone_number.strip())
    # Якщо номер починається з +, залишаємо його, інакше додаємо +
    if sanitized_number.startswith("+"):
        normalized_number = sanitized_number
    elif sanitized_number.startswith("38"):
        # Якщо номер починається з 38, додаємо +
        normalized_number = "+" + sanitized_number 
    else:
        # Інакше додаємо +38
        normalized_number = "+38" + sanitized_number
    return normalized_number


if __name__ == "__main__":
    raw_numbers = ["067 123 4567", "(095) 234-5678"]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:")
    for n in sanitized_numbers:
        print(n)


    





