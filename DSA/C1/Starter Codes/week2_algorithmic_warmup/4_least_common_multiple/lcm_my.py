# Uses python3
import sys


def gcd_fast(a, b):
    if b == 0:
        return a
    else:
        return gcd_fast(b, a % b)


def lcm_fast(a, b):
    return int((a * b) / gcd_fast(a, b))


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
