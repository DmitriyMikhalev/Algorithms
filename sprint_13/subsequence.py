"""
Gosha likes to play the game "Subsequence": 2 lines are given, and you need to
understand whether the first of them is a subsequence of the second. When the
lines are long enough, it is very difficult to get an answer to this question
just by looking at them. Help Gaucher write a function that solves this
problem.

Input format
The first line contains the string s.
In the second - string t.
Both lines consist of small Latin letters, the length of the lines does not
exceed 150,000. Lines cannot be empty.

Output format
Output True if s is a subsequence of t, otherwise -- False.

>>> solution('abc', 'ahbgdcu')
True

>>> solution('abcp', 'ahpc')
False
"""


def main() -> None:
    sub = input()
    s = input()
    print(solution(sub, s))


def solution(sub: str, s: str) -> bool:
    start = -1
    for i in sub:
        start = s.find(i, start+1)
        if start == -1:
            return False

    return True


if __name__ == '__main__':
    main()
