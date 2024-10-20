# Параметры
disk_capacity_mb = 1.44  # объем дискеты в Мб
pages_per_book = 100      # количество страниц в книге
lines_per_page = 50       # количество строк на странице
chars_per_line = 25       # количество символов в строке
bytes_per_char = 4        # байты на символ

# Переводим объем дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024

# Рассчитываем объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Рассчитываем, сколько книг помещается на дискету
num_books = disk_capacity_bytes // book_size_bytes

# Выводим результат
print(f"На дискету можно поместить {int(num_books)} одинаковых книг.")