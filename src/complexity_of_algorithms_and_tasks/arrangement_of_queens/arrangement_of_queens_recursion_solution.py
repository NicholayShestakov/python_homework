from math import factorial


def recursion_arrangement(available_coords, queens_not_arranged):
    if queens_not_arranged == 0:
        return 1
    if available_coords == []:
        return 0

    count = 0
    # Перебор каждого варианта постановки ферзя в доступную клетку
    for queen_coord in available_coords:
        # Создание нового списка доступных полей, с учётом поставленного ферзя (подробно про условия есть в решении перебором)
        new_available_coords = [
            available_coord
            for available_coord in available_coords
            if (available_coord[0] != queen_coord[0])
            and (available_coord[1] != queen_coord[1])
            and (
                available_coord[0] - available_coord[1]
                != queen_coord[0] - queen_coord[1]
            )
            and (sum(available_coord) != sum(queen_coord))
        ]
        count += recursion_arrangement(new_available_coords, queens_not_arranged - 1)

    return count


if __name__ == "__main__":
    n = int(input("Enter size of board: "))
    # Все возможные координаты ферзей
    coords = [[row, col] for row in range(n) for col in range(n)]

    arrangement_count_with_account_of_order_of_placement = recursion_arrangement(
        coords, n
    )
    # Функция считает с учётом порядка постановки ферзей, поэтому делим на факториал их количества, чтобы получить верный ответ
    arrangement_count = (
        arrangement_count_with_account_of_order_of_placement // factorial(n)
    )
    print(f"Count of right arrangements: {arrangement_count}")
