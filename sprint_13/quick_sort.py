from random import choice


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


def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = choice(array)
    left, center, right = partition(array, pivot)

    return quick_sort(left) + center + quick_sort(right)


def main():
    assert quick_sort([9, 3, 2, 9, 1, 13, 0]) == [0, 1, 2, 3, 9, 9, 13]
    print('It\'s working.')


if __name__ == '__main__':
    main()
