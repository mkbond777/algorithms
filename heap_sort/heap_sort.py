import random

import matplotlib.pyplot as plt


def heapify(a, size, large):
    heapify_iter = 1
    largest = large
    left = 2 * large + 1
    right = 2 * large + 2

    if left < size and a[left] > a[largest]:
        largest = left

    if right < size and a[right] > a[largest]:
        largest = right

    if largest != large:
        a[large], a[largest] = a[largest], a[large]
        heapify(a, size, largest)
        heapify_iter += 1
    return heapify_iter


def main():
    input_size, iteration = [], []
    for arr_size in range(1000, 2000, 100):
        arr = random.sample(range(1, 100000), arr_size)
        iterations = 0
        for i in range(round(arr_size / 2) - 1, -1, -1):
            count = heapify(arr, arr_size, i)
            iterations += count

        for i in range(arr_size - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            count = heapify(arr, i, 0)
            iterations += count

        input_size.append(arr_size)
        iteration.append(iterations)

        # print(input_size)
        # print(iteration)
        # print("\n")

    plt.plot(input_size, iteration, 'o-')
    plt.show()


if __name__ == "__main__":
    main()
