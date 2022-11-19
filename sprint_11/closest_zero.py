import sys


def main():
    size = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split(' ')))
    for i in get_zero_range(arr, size):
        print(i, end=' ')


def get_zero_range(arr, size):
    res = [0 for _ in range(0, size)]
    right_zero_index = left_zero_index = arr.index(0)

    for i in range(0, size):
        if arr[i] == 0:
            left_zero_index = i
            while True:
                right_zero_index += 1
                if right_zero_index == size:
                    right_zero_index = -1
                    break
                elif arr[right_zero_index] == 0:
                    break
        else:
            res[i] = min(abs(i - left_zero_index), abs(right_zero_index - i))

    return res


if __name__ == '__main__':
    main()
