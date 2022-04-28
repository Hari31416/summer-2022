def max_pairwise_product(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 * max_2


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
