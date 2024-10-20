# Список игроков
players = ["Алина", "Мария", "Евгения", "Антон", "Никита", "Иван", "Сергей", "Егор"]

# Определяем общее количество игроков
total_players = len(players)
print(f"Общее количество игроков: {total_players}")

# Разделяем игроков на две равные команды
mid_index = total_players // 2
team1 = players[:mid_index]
team2 = players[mid_index:]

# Выводим команды
print("Команда 1:", team1)
print("Команда 2:", team2)