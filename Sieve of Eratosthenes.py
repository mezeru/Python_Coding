from math import isqrt

if __name__ == "__main__":
    n = 2000
    a = [True]*n

    a[0] = False
    a[1] = False

    for i in range(2, isqrt(n)):
        if a[i]:
            for j in range(i*i, n, i):
                a[j] = False

    for i in range(0, n):
        if a[i]:
            print(i)
