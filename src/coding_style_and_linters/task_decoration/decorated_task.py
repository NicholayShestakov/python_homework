# Берём монеты нужных по условию номиналов и обрабатываем на предмет повторов. Также считываем номинал монеты для размена
if input("У вас есть отчество? (Y/n): ") == "Y":
    our_money = {
        len(string): 0 for string in input("Введите через пробел ваши ФИО: ").split()
    }
else:
    our_money = {
        len(string): 0 for string in input("Введите через пробел ваши ФИ: ").split()
    }
    our_money[19] = 0
money = int(input("Введите достоинство монеты для размена (натуральное число): "))

# Делаем словарь с ключами в виде номиналов наших монет и значениями в виде нулей.
# Затем мы возможно будем его использовать для подсчёта количества каждой монеты.
our_money = {key: value for key, value in our_money.items() if key <= money}

# Если у нас нету монет никаких номиналов, то выводим код ошибки.
if len(our_money) == 0:
    print("-42!")
# Если монета одна, то смотрим на кратность монеты для размена нашей монете.
elif len(our_money) == 1:
    if money % min(our_money) == 0:
        print(f"Кол-во {min(our_money)} - {money // min(our_money)}")
    else:
        print("-42!")
# Если монеты две, то считаем по алгоритму заполнения по максимуму более крупными монетами,
# с последующим вычитанием крупных монет и прибавкой мелких.
elif len(our_money) == 2:
    our_money[max(our_money)] = money // max(our_money)

    while our_money[max(our_money)] >= 0:
        our_money_sum = sum(key * value for key, value in our_money.items())

        if our_money_sum == money:
            print(
                "\n".join(f"Кол-во {key} - {value}" for key, value in our_money.items())
            )
            break

        if our_money_sum + our_money[min(our_money)] > money:
            our_money[max(our_money)] -= 1
        else:
            our_money[min(our_money)] += 1
    else:
        print("-42!")
# Если монеты три, то происходит нечто по типу полного перебора, который я не исправил до сих пор, но скоро сделаю.
else:
    max_money = max(our_money)
    min_money = min(our_money)
    mid_money = sum(our_money.keys()) - max_money - min_money
    flag = False

    for min_count in range(0, money // min_money + 1):
        for mid_count in range(0, money // mid_money + 1):
            if min_count * min_money + mid_count * mid_money > money:
                break
            for max_count in range(0, money // max_money + 1):
                if min_count + mid_count + max_count > money:
                    break
                if (
                    min_count * min_money
                    + mid_count * mid_money
                    + max_count * max_money
                    == money
                ):
                    print(f"Кол-во {min_money} - {min_count}")
                    print(f"Кол-во {mid_money} - {mid_count}")
                    print(f"Кол-во {max_money} - {max_count}")
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    else:
        print("-42!")
