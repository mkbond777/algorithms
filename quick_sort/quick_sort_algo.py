import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def main():
    for arr_size in range(100, 200, 10):
        arr = random.sample(range(1, 100000), arr_size)
        quick_sort(arr, 0, arr_size - 1)
        print(arr)
        print('\n')


if __name__ == "__main__":
    main()
