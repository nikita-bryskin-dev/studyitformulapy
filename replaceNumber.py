# Список чисел с пропущенным элементом (представленным как None)
numbers = [10, 20, None, 40, 50]

# Находим индекс пропущенного элемента и создаем новый список без него
missing_index = numbers.index(None)
valid_numbers = [num for num in numbers if num is not None]

# Вычисляем среднее арифметическое остальных элементов
mean_value = sum(valid_numbers) / len(valid_numbers)

# Заменяем пропущенный элемент средним арифметическим
numbers[missing_index] = int(mean_value)

# Выводим результат
print("Обновленный список:", numbers)