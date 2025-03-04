"""
Перша партія роботів готова, тепер їх треба перевірити. Усі роботи унікальні, і швидкість руху в кожного своя. У цьому завданні тобі потрібно знайти найменшу, найбільшу та середню швидкості роботів.

Напиши функцію get_speed_statistic(), яка:

Приймає список швидкостей роботів test_results.
Повертає статистику у вигляді списку, у якому:
перший елемент — найменша швидкість;
другий елемент — найбільша швидкість;
третій елемент — середнє значення, округлене вниз (використай from math import floor).
💡 Якщо вхідний список швидкостей порожній, поверни [0, 0, 0].

Наприклад:
get_speed_statistic([]) # [0, 0, 0]
get_speed_statistic([10]) # [10, 10, 10]
get_speed_statistic([8, 9, 3, 12]) # [3, 12, 8]
get_speed_statistic([10, 10, 11, 9, 12, 8]) # [8, 12, 10]
"""

from math import floor


def get_speed_statistic(test_results):
    # write your code here
    try:
        highest = max(test_results)
        lowest = min(test_results)
        average = sum(test_results) / len(test_results)
        return [lowest, highest, floor(average)]
    except ValueError:
        return [0, 0, 0]


result = get_speed_statistic([10, 10, 11, 9, 12, 8])
print(result)