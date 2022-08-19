n = 22
terms = []

while n != 1:
    if n % 2 == 0:
        n = n / 2
        terms.append(int(n))
    else:
        n = 3 * n + 1
        terms.append(int(n))

print(terms)