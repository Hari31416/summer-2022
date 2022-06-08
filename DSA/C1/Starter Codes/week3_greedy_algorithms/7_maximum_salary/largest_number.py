# Uses python3

import sys


def largest_number(nums):
    def key(x):
        x = str(x)
        if len(x) != 1:
            return int(f"{x}{'0'*(3-len(x))}")
        else:
            return int(f"{x}90")

    nums.sort(key=key, reverse=True)
    return int("".join(str(x) for x in nums))


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
