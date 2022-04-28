# Uses python3
def fibo_fast(n):
    if n<=1:
        return n
        
    zeros = [0]*(n-1)
    nums = [0, 1]
    nums.extend(zeros)
    for i in range(2, n+1):
        nums[i] = (nums[i-1]+ nums[i-2])

    return nums[n]

if __name__ == '__main__':
    print(fibo_fast(int(input())))
