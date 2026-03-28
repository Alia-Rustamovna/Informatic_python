# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator = ','):
    participants_first = set(participants_first_group.split( separator))
    participants_second = set(participants_second_group.split( separator))
    common_participants = participants_first.intersection(participants_second)
    common_participants_list = list(common_participants)
    common_participants_list.sort()
    return common_participants_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group,'|')
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
