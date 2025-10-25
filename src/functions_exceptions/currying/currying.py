def curry(func, n):
    if n < 0:
        raise Exception("Negative n-ary.")
    try:
        func(*range(n))
    except TypeError:
        raise Exception("Not right n-ary.")

    if n in (0, 1):
        return func

    def curried_func(x):
        def new_func(*args):
            return func(x, *args)

        return curry(new_func, n - 1)

    return curried_func


def uncurry(curried_func, n):
    if n < 0:
        raise Exception("Negative n-ary.")

    if n == 0:
        return curried_func

    def uncurried_func(*args):
        new_func = curried_func(args[0])
        for x in range(1, n):
            new_func = new_func(args[x])

        return new_func

    try:
        uncurried_func(*range(n))
    except TypeError:
        raise Exception("Not right n-ary.")

    return uncurried_func
