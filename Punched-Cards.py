num_cases = int(input())
RC = ""
for i in range(num_cases):
    RC = list(map(int, input().strip().split(" ")))
    R = int(RC[0])
    C = int(RC[1])
    first_R = ('.'*2 + ('+-'*(C-1)) + '+\n')
    second_R = ('.'*2 + ('|.'*(C-1)) + '|\n')    
    middle_R = (('+-'*C + '+\n') + ('|.'*C + '|\n'))*(R-1)
    last_R = ('+-'*C + '+')
    matrix = "\n" + first_R + second_R + middle_R + last_R
    print("Case #{}: {}".format(i+1,matrix))
