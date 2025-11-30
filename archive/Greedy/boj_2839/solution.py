n = int(input())

if n == 3:
    print(1)
    exit()
elif n == 4:
    print(-1)
    exit()
elif n == 5:
    print(1)
    exit()

five_share = n // 5
five_remainder = n % 5

if five_remainder == 0:
    print(five_share)
    exit()

while five_share >= 0:
    three_share = five_remainder // 3
    three_remainder = five_remainder % 3

    if three_remainder == 0:
        print(five_share + three_share)
        exit()

    five_share -= 1
    five_remainder += 5


print(-1)
    

