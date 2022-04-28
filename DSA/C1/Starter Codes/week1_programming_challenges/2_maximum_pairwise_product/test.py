import random


def max_pairwise_product(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 * max_2


def max_pairwise_product_slow(numbers):
    number = 0
    for count, i in enumerate(numbers):
        for j in numbers[count + 1 :]:
            if i * j > number:
                number = i * j
    return number


if __name__ == "__main__":
    input_n = random.randint(0, 3) + 2
    input_numbers = [random.randint(0, 100) for i in range(input_n)]
    print(input_n)
    print(input_numbers)
    slow_answer = max_pairwise_product_slow(input_numbers)
    fast_answer = max_pairwise_product(input_numbers)
    print(input_numbers)
    print(slow_answer, fast_answer)
    # while True:
    #     input_n = random.randint(0, 3) + 2
    #     input_numbers = [random.randint(0, 100) for i in range(input_n + 1)]
    #     slow_answer = max_pairwise_product_slow(input_numbers)
    #     fast_answer = max_pairwise_product(input_numbers)
    #     print(input_n)
    #     print(input_numbers)
    #     print(slow_answer, fast_answer)
    #     if slow_answer != fast_answer:
    #         break
    # print(max_pairwise_product(input_numbers))
