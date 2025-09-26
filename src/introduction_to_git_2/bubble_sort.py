def bubble_sort(lst):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                not_sorted = True
    
    return lst


if __name__ == "__main__":
    print("Enter list of numbers separated by space: ", end="")
    lst = [int(number) for number in input().split()]
    lst = bubble_sort(lst)
    print(" ".join([str(number) for number in lst]))
