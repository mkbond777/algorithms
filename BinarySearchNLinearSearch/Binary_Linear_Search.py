import random


def get_mid(arr, low_ind, high_ind):
    return arr[round((low_ind + high_ind) / 2)]


def binary_search(arr, length, key):
    print("key element is %d and index is %d" % (key, arr.index(key) + 1))
    low = arr[0]
    high = arr[length - 1]
    mid = get_mid(arr, 0, length - 1)

    while low < high:
        print("mid_element is : " + str(mid))
        if mid > key:
            high = arr[arr.index(mid) - 1]
            mid = get_mid(arr, arr.index(low), arr.index(high))
        elif mid < key:
            low = arr[arr.index(mid) + 1]
            mid = get_mid(arr, arr.index(low), arr.index(high))
        else:
            break

    print("binary search: element found at : " + str(arr.index(mid) + 1))


def linear_search(arr, length, key):
    for i in range(length):
        if arr[i] == key:
            print("linear search : element found at : " + str(i + 1))
            break


def main():
    n = 1000
    a = sorted(random.sample(range(1, 100000), n))
    key = random.choice(a)
    binary_search(a, n, key)
    linear_search(a, n, key)

if __name__ == "__main__":
    main()
