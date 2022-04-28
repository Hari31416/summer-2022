import sys

n = sys.argv[1]
# print(n)
nums = list(range(int(n)))
print(" ".join(str(x) for x in nums))
