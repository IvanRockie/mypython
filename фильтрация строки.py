def filter_string(string, symbol):
    result = ''
    index = 0
    while index < len(string):  # Пока индекс меньше длины строки
        if string[index] != symbol:  # Если текущий символ не равен удаляемому
            result += string[index]  # Добавляем его в результат
        index += 1  # Увеличиваем индекс

    return result

# Пример вызова
text = 'If I look back I am lost'
print(filter_string(text, 'I'))  # 'f  look back  am lost'
print(filter_string(text, 'o'))  # 'If I lk back I am lst'
