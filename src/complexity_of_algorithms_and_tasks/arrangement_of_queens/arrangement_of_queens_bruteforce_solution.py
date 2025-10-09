from itertools import combinations

if __name__ == "__main__":
    n = int(input("Enter size of board: "))
    # Все возможные координаты ферзей
    coords = [[row, col] for row in range(n) for col in range(n)]
    count = 0

    # Перебор всех выборок из n ферзей
    for current_coords in combinations(coords, n):
        # Перебор всех пар в каждой выборке
        for pair in combinations(current_coords, 2):
            coord1, coord2 = pair
            # Проверка каждой пары на то, что они друг друга не бьют
            if (
                (coord1[0] == coord2[0])  # Проверка на одинаковую строку
                or (coord1[1] == coord2[1])  # Проверка на одинаковый столбец
                or (
                    coord1[0] - coord1[1] == coord2[0] - coord2[1]
                )  # Проверка на одинаковую диагональ, параллельную главной
                or (
                    sum(coord1) == sum(coord2)
                )  # Проверка на одинаковую диагональ, перпендикулярную главной
            ):
                break
        else:
            count += 1

    print(f"Count of right arrangements: {count}")
