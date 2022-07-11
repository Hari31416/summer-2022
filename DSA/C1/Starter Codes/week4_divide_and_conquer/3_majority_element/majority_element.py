# Uses python3
import sys


def majority(arr):
    arr.sort()
    el_c = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] == el_c:
            cnt += 1
        else:
            cnt = 1
            el_c = arr[i]

        if cnt > len(arr) // 2:
            return el_c
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majority(a) != -1:
        print(1)
    else:
        print(0)
