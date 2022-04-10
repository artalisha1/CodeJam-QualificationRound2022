num_cases = int(input())
for i in range(num_cases):
    num_dice = int(input())
    dice = list(map(int, input().strip().split(" ")))
    dice.sort()
    straight = 1
    for num in dice:
        if straight <= num:
            straight += 1
        else:
            num_dice -= 1
    print("Case #{}: {}".format(i+1, num_dice))
