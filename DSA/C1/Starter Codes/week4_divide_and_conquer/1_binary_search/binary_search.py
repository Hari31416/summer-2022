def binary_search(input_keys, q):
    def binary_search_main(array, low, high, key):
        if array[0] == key:
            return 0
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if array[mid - 1] == key:
            return mid - 1
        if array[mid - 1] > key:
            return binary_search_main(array, low, mid - 1, key)
        else:
            return binary_search_main(array, mid + 1, high, key)

    return binary_search_main(array=input_keys, low=0, high=len(input_keys), key=q)


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")
