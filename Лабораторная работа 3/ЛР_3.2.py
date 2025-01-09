# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки участников по заданному разделителю
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников с помощью пересечения множеств
    common_participants = participants1.intersection(participants2)
    # Сортируем участников в алфавитном порядке и возвращаем в виде списка
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызов функции с разделителем '|'
result = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(result)

