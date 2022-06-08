# Uses python3
import sys


def optimal_summands(n):
    if n == 1:
        return [1]
    summands = []
    n_cur = n
    n_prev = n
    for i in range(1, int(n / 2) + 2):
        n_cur = n_prev - i

        if n_cur - (i + 1) < 0:
            summands.append(n_prev)
            break
        n_prev = n_cur
        if i not in summands[-4:]:
            summands.append(i)
        else:
            break
    assert sum(summands) == n
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
