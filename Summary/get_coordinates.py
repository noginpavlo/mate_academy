"""
Ускладнюємо роботу нашого робота! Тепер він вміє перетворювати команди руху на правильний сигнал і рухатися відповідно до нього:

"forward" означає y + 1 (крок уперед);
"back" означає y - 1 (крок назад);
"right" означає x + 1 (крок праворуч);
"left" означає x - 1 (крок ліворуч).
Але було б чудово, якби робот знав, де він знаходиться навіть без GPS. Для цього реалізуй функцію get_location(), яка:

Приймає 2 параметри:
список початкових координат coordinates у вигляді [x, y];
список із командами commands у вигляді ["command1", "command2", "command3" ...].
Повертає список кінцевих координат [x, y] після рухів згідно з командами зі списку commands.
Наприклад, ми маємо список із координатами coordinates = [2, 1] та список із командами commands = ["left", "back", "back"]:

координати після першої команди — [1, 1] (1 крок ліворуч);
координати після другої команди — [1, 0] (1 крок назад);
координати після третьої команди — [1, -1] (1 крок назад);
результатом буде список [1, -1].
Ще приклади:

get_location([0, 0], ["forward", "right"])  # [1, 1]
get_location([2, 3], ["back", "back", "back", "right"])  # [3, 0]
get_location([0, 5], ["back", "back", "back", "right", "left", "forward"])  # [0, 3]

"""
coord = [0, 5]
comm = ["back", "back", "back", "right", "left", "forward"]

# answer should == [0, 3]

def get_location(coordinates, commands):
    # write your code here
    for command in commands:
        if command == "forward":
            coordinates[1] += 1
        elif command == "back":
            coordinates[1] -= 1
        elif command == "right":
            coordinates[0] += 1
        elif command == "left":
            coordinates[0] -= 1
    return coordinates

result = get_location(coord, comm)
print(result)