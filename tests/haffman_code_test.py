from haffman_code.haffman_code import encode, decode, file_encode, file_decode
from random import randint
from pathlib import Path


def test_encode_decode_biection():
    string = "".join(chr(randint(128, 255)) for _ in range(randint(1, 1000)))
    encoded_string, table = encode(string)
    assert string == decode(encoded_string, table)


def test_encode_decode_empty_biection():
    encoded_string, table = encode("")
    assert "" == decode(encoded_string, table)


def test_encode_uniqueness():
    string = "".join(chr(randint(128, 255)) for _ in range(randint(1, 1000)))
    table = encode(string)[1]
    codes = table.keys()
    for code in codes:
        for other_code in codes:
            if code == other_code:
                continue
            if code == other_code[: len(code)]:
                assert False
                break
    else:
        assert True


def test_file_encode_decode_biection():
    Path("./haffman_code_test_files").mkdir(exist_ok=True)
    string = "".join(chr(randint(128, 255)) for _ in range(randint(1, 1000)))
    with open("haffman_code_test_files/haffman_code_test_text_file.txt", "w") as file:
        file.write(string)

    file_encode("haffman_code_test_files/haffman_code_test_text_file.txt")
    file_decode("haffman_code_test_files/haffman_code_test_text_file.encoded")

    with open(
        "haffman_code_test_files/decoded-haffman_code_test_text_file.txt", "r"
    ) as decoded_file:
        assert string == decoded_file.read()


def test_file_encode_decode_empty_biection():
    Path("./haffman_code_test_files").mkdir(exist_ok=True)
    string = ""
    with open("haffman_code_test_files/haffman_code_test_text_file.txt", "w") as file:
        file.write(string)

    file_encode("haffman_code_test_files/haffman_code_test_text_file.txt")
    file_decode("haffman_code_test_files/haffman_code_test_text_file.encoded")

    with open(
        "haffman_code_test_files/decoded-haffman_code_test_text_file.txt", "r"
    ) as decoded_file:
        assert string == decoded_file.read()
