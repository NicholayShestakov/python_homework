from rewriting_hw_1.walker_scheme import WalkerScheme


def test_exception():
    try:
        scheme = WalkerScheme([("A", 0.1), ("B", 1)])
    except Exception as e:
        assert str(e) == "Сумма вероятностей не равна 1."
