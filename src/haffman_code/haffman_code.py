from pathlib import Path


def encode(msg: str) -> tuple[str, dict[str, str]]:
    """Haffman code encoder."""
    # Подстчёт количества каждого символа и преобразование в список кортежей, сортированный по частоте.
    char_count = {}
    for char in msg:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_count_list = sorted(char_count.items(), key=lambda item: item[1])

    code_table = {char: "" for char in msg}
    while len(char_count_list) > 1:
        char_count_list = sorted(char_count_list, key=lambda item: item[1])

        # Берём две самые минимальные штуки
        smallest_one = char_count_list.pop(0)
        smallest_two = char_count_list.pop(0)
        # Перебор и обработка всех символов, которые на этих ветках.
        for char in smallest_one[0]:
            code_table[char] = "0" + code_table[char]
        for char in smallest_two[0]:
            code_table[char] = "1" + code_table[char]

        merged_element = (
            smallest_one[0] + smallest_two[0],
            smallest_one[1] + smallest_two[1],
        )
        char_count_list.append(merged_element)

    encoded_msg = ""
    for char in msg:
        encoded_msg += code_table[char]

    decode_table = {haffman: char for char, haffman in code_table.items()}

    return encoded_msg, decode_table


def decode(encoded: str, table: dict[str, str]) -> str:
    """Haffman code decoder."""
    decoded = ""
    current_element = ""
    for digit in encoded:
        current_element += digit
        if current_element in table:
            decoded += table[current_element]
            current_element = ""

    return decoded


def file_encode(filepath: str):
    """Haffman code file encoder. Creates encoded file with name "filename.encoded". If file with this name already exists, replaces it."""
    path = Path(filepath)

    if not path.is_file():
        raise Exception("File doesn`t exist.")

    with open(path, "r") as file:
        with open(str(path.parent) + "/" + path.stem + ".encoded", "w") as encoded_file:
            encoded_msg, table = encode(file.read())
            # Обработка таблицы в строку, где через пробелы идут склеенные символ и его код.
            string_table = " ".join([item[1] + item[0] for item in table.items()])

            encoded_file.write(encoded_msg + "\n")
            encoded_file.write(string_table)


def file_decode(filepath: str):
    """Haffman code file decoder. Creates decoded file with name "decoded-'filename'.txt". If file with this name already exists, replaces it.\n
    Takes only "*.encoded" files."""
    path = Path(filepath)

    if not path.is_file():
        raise Exception("File doesn`t exist.")
    if path.suffix != ".encoded":
        raise Exception("File suffix isn`t '.encoded'.")

    with open(path, "r") as encoded_file:
        with open(
            str(path.parent) + "/decoded-" + path.stem + ".txt", "w"
        ) as decoded_file:
            # Получение данных, где только одно разделение, поскольку среди закодированных символов может быть "\n"
            encoded_msg, string_table = encoded_file.read().split("\n", maxsplit=1)
            # Проверка на пустоту файла
            if encoded_msg == "":
                decoded_file.write("")
            else:
                # Обработка таблицы в словарь из строки.
                splitted_string_table = string_table.split(" ")
                # Если есть, значит среди символов был пробел, которого мы вот таким вот костылём чиним.
                if "" in splitted_string_table:
                    space_index = splitted_string_table.index("")
                    splitted_string_table.pop(space_index)
                    splitted_string_table[space_index] = (
                        " " + splitted_string_table[space_index]
                    )

                table = {item[1:]: item[0] for item in splitted_string_table}

                decoded_file.write(decode(encoded_msg, table))


# Честно говоря, про возможность работы в бинарном режиме я не забыл, но не нашёл применения для него.
