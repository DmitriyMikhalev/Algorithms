def binary_search_recursive(array, to_find, left_index, right_index):
    """Find index of element using recursive binary search. If it doesn't
    exist, return -1.
    [left, mid), [mid, right) so mid is always at right sequence.
    """
    if left_index >= right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if array[mid_index] == to_find:
        return mid_index
    elif to_find > array[mid_index]:
        return binary_search_recursive(
                array,
                to_find,
                mid_index + 1,
                right_index
            )
    else:
        return binary_search_recursive(
            array,
            to_find,
            left_index,
            mid_index
            )


def main():
    test()


def test():
    arr = [1, 3, 5, 6, 7, 13, 93, 104, 491, 49192, 99999]
    right = len(arr)
    left = 0
    assert binary_search_recursive(arr, 1, left, right) == 0
    assert binary_search_recursive(arr, 99999, left, right) == 10
    assert binary_search_recursive(arr, 93, left, right) == 6
    assert binary_search_recursive(arr, -1, left, right) == -1
    print('Algorithm is working.')


if __name__ == '__main__':
    main()
