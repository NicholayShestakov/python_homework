from testing_pytest_base.heap_sort.heap_sort import heap_sort
import random


def test_common():
    lst = [3, 1, 2]
    heap_sort(lst)
    assert lst == [1, 2, 3]


def test_empty():
    lst = []
    heap_sort(lst)
    assert lst == []


def test_another_sort():
    lst = [random.randint(-1000000, 1000000) for _ in range(10000)]
    sorted_with_another = sorted(lst)
    heap_sort(lst)
    assert lst == sorted_with_another
