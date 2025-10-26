from functions_exceptions.currying.currying import curry, uncurry


def test_base():
    def func(x, y, z):
        return x + y + z

    curry_func = curry(func, 3)
    uncurry_func = uncurry(curry_func, 3)
    assert func(10, 20, 30) == curry_func(10)(20)(30) == uncurry_func(10, 20, 30)


def test_unknown_argument_count():
    def func(*args):
        return sum(args)

    curry_func = curry(func, 5)
    uncurry_func = uncurry(curry_func, 5)
    assert (
        func(1, 2, 3, 4, 5) == curry_func(1)(2)(3)(4)(5) == uncurry_func(1, 2, 3, 4, 5)
    )


def test_no_arguments():
    def func():
        return 1

    curry_func = curry(func, 0)
    uncurry_func = uncurry(curry_func, 0)
    assert func() == curry_func() == uncurry_func()


def test_one_argument():
    def func(x):
        return x

    curry_func = curry(func, 1)
    uncurry_func = uncurry(curry_func, 1)
    assert func(1) == curry_func(1) == uncurry_func(1)


def test_curry_negative_n_ary():
    def func(x, y, z):
        return x + y + z

    try:
        curry(func, -1)
    except Exception as e:
        assert str(e) == "Negative n-ary."


def test_uncurry_negative_n_ary():
    def func(x, y, z):
        return x + y + z

    try:
        curry_func = curry(func, 3)
        uncurry(curry_func, -1)
    except Exception as e:
        assert str(e) == "Negative n-ary."


def test_curry_not_right_n_ary():
    def func(x, y, z):
        return x + y + z

    try:
        curry(func, 4)
    except Exception as e:
        assert str(e) == "Not right n-ary."


def test_uncurry_not_right_n_ary():
    def func(x, y, z):
        return x + y + z

    try:
        curry_func = curry(func, 3)
        uncurry(curry_func, 4)
    except Exception as e:
        assert str(e) == "Not right n-ary."
