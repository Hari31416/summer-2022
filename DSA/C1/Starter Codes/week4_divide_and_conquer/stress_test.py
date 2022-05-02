import random
import math


def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1


def binary_search(array, key):
    if len(array) == 1 and array[0] != key:
        return -1
    elif len(array) == 1 and array[0] == key:
        return 0

    middle = math.floor((len(array)) / 2)

    if key == array[middle]:
        return middle
    elif key > array[middle]:
        return binary_search(array=array[middle:], key=key)
    elif key < array[middle]:
        return binary_search(array=array[:middle], key=key)


def stress_test():
    test = 0
    while test < 1000:
        nums = [random.randint(1, 100000) for _ in range(100000)]
        nums.sort()
        key = random.randint(1, 100000)
        sol1 = linear_search(nums, key)
        sol2 = binary_search(nums, key)
        test += 1
        if sol1 == sol2:
            print("OKAY\n")
        else:
            print(f"{sol1} and {sol2}\n")


if __name__ == "__main__":
    stress_test()
