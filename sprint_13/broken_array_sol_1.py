from random import choice


def binary_search_recursive(array, to_find, left, right):
    if left >= right:
        return -1

    mid_index = (left + right) // 2
    mid_elem = array[mid_index]

    if mid_elem[0] == to_find:
        return mid_elem[1]
    elif mid_elem[0] > to_find:
        return binary_search_recursive(array, to_find, left, mid_index)
    else:
        return binary_search_recursive(array, to_find, mid_index + 1, right)


def broken_search(array, target) -> int:
    array = [[array[i], i] for i in range(len(array))]
    array = quick_sort(array)

    return binary_search_recursive(array, target, 0, len(array))


def main():
    test()


def partition(array, pivot):
    left = []
    center = []
    right = []

    for elem in array:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            center.append(elem)

    return left, center, right


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 1]
    assert broken_search(arr, 1) == 1


def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = choice(array)
    left, center, right = partition(array, pivot)

    return quick_sort(left) + center + quick_sort(right)


if __name__ == '__main__':
    main()
