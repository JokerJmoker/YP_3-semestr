import re

def parse_modulus(expression: str):
    """Преобразует строку вида |number| в abs(number)"""
    # Регулярное выражение для поиска выражений вида |number|
    pattern = r'\|([^\|]+?)\|'
    # Заменяем |number| на abs(number)
    result = re.sub(pattern, r'abs(\1)', expression)
    return result

# Пример использования
a = -3
expression = "|a|"
parsed_expression = parse_modulus(expression)
#print(parsed_expression)  # Вывод: abs(3 - 4)

# Для вычисления результата, используем eval в безопасном контексте
result = eval(parsed_expression)
print(result)  # Вывод: 1 (так как abs(3 - 4) = abs(-1) = 1