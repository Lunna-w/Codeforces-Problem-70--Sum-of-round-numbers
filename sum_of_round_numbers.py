def find_round_summands(n):
    summands = []
    position = 1

    while n > 0:
        digit = n % 10
        if digit != 0:
            summands.append(digit * position)
        n //= 10
        position *= 10

    return summands

t = int(input())

for _ in range(t):
    n = int(input())
    summands = find_round_summands(n)
    print(len(summands))
    print(*summands)