t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_digit = min(a)
    min_index = a.index(min_digit)  # Find the index of the minimum digit
    a[min_index] += 1  # Increment the minimum digit by 1

    prod = 1
    for digit in a:
        prod *= digit

    print(prod)
