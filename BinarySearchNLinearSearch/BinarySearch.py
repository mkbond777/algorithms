import random

n = 1000
a = sorted(random.sample(range(1, 100000), n))


def get_mid(arr, low_ind, high_ind):
    return arr[round((low_ind + high_ind) / 2)]


key = random.choice(a)
print("key element is %d and index is %d" % (key, a.index(key)+1))
low = a[0]
high = a[n - 1]
mid = get_mid(a, 0, n-1)

while low < high:
    print("mid_element is : " + str(mid))
    if mid > key:
        high = a[a.index(mid)-1]
        mid = get_mid(a, a.index(low), a.index(high))
    elif mid < key:
        low = a[a.index(mid)+1]
        mid = get_mid(a, a.index(low), a.index(high))
    else:
        break

print("element found at : " + str(a.index(mid)+1))
