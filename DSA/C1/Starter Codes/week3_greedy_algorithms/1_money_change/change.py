# Uses python3
import sys

def get_change(m):
    denominations = [10, 5]
    coins = 0
    remaining = m
    for d in denominations:
        remainder = remaining%d
        coin = int((remaining-remainder)/d)
        coins+=coin
        remaining = remaining - coin*d
    return coins + remaining

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
