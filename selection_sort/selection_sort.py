import random


def select_sort(a, length):
    count = 0
    for i in range(0, length):
        temp = i
        count += 1
        for j in range(i + 1, length):
            count += 1
            if a[j] < a[i]:
                temp = j
        a[i], a[temp] = a[temp], a[i]
    return count


def main():
    for n in range(1000, 10000, 1000):
        arr = random.sample(range(1, 1000000), n)
        count = select_sort(arr, n)
        print("array size %d has complexity %d" % (n, count))


if __name__ == "__main__":
    main()
