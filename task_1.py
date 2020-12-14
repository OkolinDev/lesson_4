# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

task_1, per_hour, output_hours = argv
print('Имя скрипта: ', task_1)
try:
    per_hour = int(per_hour)
    output_hours = int(output_hours)
    total = per_hour * output_hours
    bonus = (total / 100) * 20
    total_var = total + bonus
    print('Ваш оклад: ', total)
    print('Ваша премия: ', bonus)
    print('Ваша зарплата состаявляет: ', total_var)
except ValueError:
    print('Данные некорректны')
