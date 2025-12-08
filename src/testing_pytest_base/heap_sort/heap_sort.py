def _heapify(lst, index):
    while index > 0:
        if lst[index] > lst[(index - 1) // 2]:
            temp = lst[index]
            lst[index] = lst[(index - 1) // 2]
            lst[(index - 1) // 2] = temp
        else:
            break
        index = (index - 1) // 2


def _list_to_heap(lst, unsorted_size):
    for i in range(unsorted_size):
        if lst[i] > lst[(i - 1) // 2]:
            _heapify(lst, i)


def heap_sort(lst):
    """Standart heap sorting algorithm. Takes list and sorts it."""
    size = len(lst)
    for i in range(size):
        _list_to_heap(lst, size - i)
        temp = lst[0]
        lst[0] = lst[size - i - 1]
        lst[size - i - 1] = temp


if __name__ == "__main__":
    lst = list(map(int, input("Input list: ").split()))
    heap_sort(lst)
    print(lst)
