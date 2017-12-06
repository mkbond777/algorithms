def knapsack(W, wt, val, leng):
    if leng == 0 or W == 0:
        return 0
    if wt[leng - 1] > W:
        return knapsack(W, wt, val, leng - 1)
    else:
        return max(val[leng - 1] + knapsack(W - wt[leng - 1], wt, val, leng - 1), knapsack(W, wt, val, leng - 1))


def main():
    val = [60, 100, 120, 180]
    wt = [10, 20, 30, 40]
    W = 50
    n = len(wt)
    print(knapsack(W, wt, val, n))


if __name__ == "__main__":
    main()
