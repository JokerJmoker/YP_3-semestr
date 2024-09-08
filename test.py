def is_prime(n):
    """Проверяет, является ли число простым"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Пример использования
number = 29
print(f"Число {number} {'является' if is_prime(number) else 'не является'} простым.")
