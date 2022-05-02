#Uses python3

import sys

def largest_number(a):
    single_nums = []
    for n in a:
        for m in list(str(n)):
            single_nums.append(int(m))
    single_nums.sort(reverse=True)
    nums = [str(i) for i in single_nums]
    return int("".join(nums))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
