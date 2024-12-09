def join_numbers_from_range(start, finish):
    result = ""  # Инициализируем как пустую строку
    i = start    # Начинаем с `start`

    while i <= finish:
        result = result + str(i)  # Преобразуем число в строку и добавляем
        i = i + 1

    return result

print(join_numbers_from_range(1,1))
print(join_numbers_from_range(2,3))
print(join_numbers_from_range(1, 10))  # "12345678910"
