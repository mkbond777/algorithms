a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_mid(arr, low_ele, high_element):
    return arr[round((arr.index(low_ele) + arr.index(high_element)) / 2+0.5)]


key = 1
low = a[0]
high = a[len(a) - 1]
mid = get_mid(a, low, high)

while low < high:
    print("mid_element is : " + str(mid))
    if mid > key:
        high = mid
        mid = get_mid(a, low, high)
    elif mid < key:
        low = mid
        mid = get_mid(a, low, high)
    else:
        break

print("element found at : " + str(a.index(mid)+1))
