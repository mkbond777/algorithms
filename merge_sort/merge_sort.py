import random

iterations = 0


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    count = 0

    # create temp array
    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(0, n1):
        left_arr[i] = arr[l + i]
        count += 1
    for j in range(0, n2):
        right_arr[j] = arr[m + 1 + j]
        count += 1

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        count += 1
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
        count += 1
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1
        count += 1
    return count


def merge_sort(arr, first, last):
    global iterations
    if first < last:
        m = round((first + (last - 1)) / 2)
        merge_sort(arr, first, m)
        merge_sort(arr, m + 1, last)
        iterations = iterations + merge(arr, first, m, last)
    return iterations


def main():
    for arr_size in range(1000, 2000, 100):
        arr = random.sample(range(1, 100000), arr_size)
        count = merge_sort(arr, 0, arr_size - 1)
        print(arr)
        print(count)
        print('\n')


if __name__ == "__main__":
    main()
