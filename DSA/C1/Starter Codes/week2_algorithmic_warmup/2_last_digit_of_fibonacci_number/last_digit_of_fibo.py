# Uses python3
def fibo_last_digit(n):
    if n <= 1:
        return n

    zeros = [0] * (n - 1)
    nums = [0, 1]
    nums.extend(zeros)
    for i in range(2, n + 1):
        nums[i] = (nums[i - 1]) % 10 + (nums[i - 2]) % 10

    return int(str(nums[n])[-1])


if __name__ == "__main__":
    print(fibo_last_digit(int(input())))
