def main():
    test()
    print('It\'s working.')


def merge(arr: list, left: int, mid: int, right: int):
    """[left, mid), [mid, right)"""
    arr_1 = arr[left:mid]
    arr_2 = arr[mid:right]
    i = j = 0
    curr_res = left

    while i != len(arr_1) and j != len(arr_2):
        if arr_1[i] <= arr_2[j]:
            arr[curr_res] = arr_1[i]
            i += 1
        else:
            arr[curr_res] = arr_2[j]
            j += 1
        curr_res += 1

    while i != len(arr_1):
        arr[curr_res] = arr_1[i]
        i += 1
        curr_res += 1

    while j != len(arr_2):
        arr[curr_res] = arr_2[j]
        j += 1
        curr_res += 1

    return arr


def merge_sort(arr, left, right):
    """[lf, rg)"""
    if right - left == 1:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    main()
