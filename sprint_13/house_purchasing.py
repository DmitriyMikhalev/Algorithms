"""
Timofey decided to buy several houses on the famous Algos archipelago among
developers. He found n ads for sale, where the cost of each house is indicated
in Argos francs. And Timofey has k francs. Help him determine what is the
largest number of houses on Algos he will be able to purchase for this money.

Input format
The first line contains the natural numbers n and k separated by a space.

n is the number of houses that Timothy is considering, it does not exceed
100,000;

k — total budget, does not exceed 100,000;

In the next line, separated by a space, n house values are written. Each of the
numbers does not exceed 100,000. All values are natural numbers.

Output format
Print one number - the largest number of houses that Timofey can buy.

>>> solution([999, 999, 999], 900)
0

>>> solution([350, 999, 200], 1000)
2
"""


def main() -> None:
    _, money = map(int, input().split(' '))
    prices = [int(i) for i in input().split(' ')]
    print(solution(prices, money))


def merge(arr: list, left: int, mid: int, right: int) -> list[int]:
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


def merge_sort(arr, left, right) -> None:
    """[lf, rg)"""
    if right - left == 1:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


def solution(prices: list[int], money: int) -> int:
    merge_sort(prices, 0, len(prices))
    count = 0
    for price in prices:
        if price > money:
            break
        count += 1
        money -= price

    return count


if __name__ == '__main__':
    main()
