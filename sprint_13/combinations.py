def concat(seq, string, res):
    buttons = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if len(seq) == 0:
        res.append(string)
        return
    for char in buttons[seq[0]]:
        string += char
        concat(seq[1:], string, res)
        string = string[:-1]


def get_combinations(seq):
    res = []
    concat(seq, '', res)
    for i in res:
        print(i, end=' ')


def main():
    sequence = input()
    get_combinations(sequence)


if __name__ == '__main__':
    main()
