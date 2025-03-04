"""
А тепер настав час збільшити обсяги виробництва роботів 🤖 🤖 🤖

Напиши функцію get_plan(), яка:

Приймає 3 параметри:
current_production — поточна кількість роботів, яку ми виробляємо за місяць;
months — кількість місяців, протягом якої виробництво має зростати;
percent — відсоток, на який має зростати виробництво щомісяця.
Повертає список із цілями на кожен місяць (скільки роботів треба виробити, щоб дотримуватись запланованого зростання).
Щоб краще зрозуміти, як це працює, розглянемо приклад. Припустимо, нам дано current_production = 200, months = 3 та percent = 50:

план на перший місяць — 200 + 50% = 300 роботів;
на другий місяць це вже 300 + 50% = 450 роботів;
і нарешті на третій місяць це 450 + 50% = 675 роботів.
у результаті маємо отримати список [300, 450, 675].
💡 Ціль на наступний місяць потрібно рахувати на основі попереднього місяця. А якщо число роботів виявиться дробовим, округли його за допомогою math.floor.

Ще приклади:
get_plan(10, 4, 30)  # [13, 16, 20, 26]
get_plan(1000, 6, 20)  # [1200, 1440, 1728, 2073, 2487, 2984]
"""
import math

def get_plan(current_production, months, percent):
    # write your code here
    my_list = []
    for month in range(months):
        current_production += current_production * percent/100
        current_production = math.floor(current_production)
        my_list.append(current_production)
    return my_list

result = get_plan(1000, 6, 20)
print(result)