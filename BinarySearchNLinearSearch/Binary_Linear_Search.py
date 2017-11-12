import random


def get_mid(arr, low_ind, high_ind):
    return arr[round((low_ind + high_ind) / 2)]


def binary_search(arr, length, key):
    print("key element is %d and index is %d" % (key, arr.index(key) + 1))
    low = arr[0]
    high = arr[length - 1]
    mid = get_mid(arr, 0, length - 1)
    i = 0

    while low < high:
        i += 1
        # print("mid_element is : " + str(mid))
        if mid > key:
            high = arr[arr.index(mid) - 1]
            mid = get_mid(arr, arr.index(low), arr.index(high))
        elif mid < key:
            low = arr[arr.index(mid) + 1]
            mid = get_mid(arr, arr.index(low), arr.index(high))
        else:
            break

    print("binary search: element found at : " + str(arr.index(mid) + 1))
    return i


def linear_search(arr, length, key):
    i = 0
    for i in range(length):
        if arr[i] == key:
            print("linear search : element found at : " + str(i + 1))
            break
    return i + 1


def main():
    for n in range(1000, 2100, 100):
        a = sorted(random.sample(range(1, 100000), n))
        print("size of the array is %d" % len(a))
        key = random.choice(a)
        b_search = binary_search(a, n, key)
        l_search = linear_search(a, n, key)
        print("b_search search took %d iteration while linear search took %d iterations for input size %d \n"
              % (b_search, l_search, n))


if __name__ == "__main__":
    main()
