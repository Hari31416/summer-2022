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


def sum_n_fibo_fast(n):
    return (fibo_last_digit(n + 2) - 1)


if __name__ == "__main__":
    n = int(input())
    print(sum_n_fibo_fast(n))
