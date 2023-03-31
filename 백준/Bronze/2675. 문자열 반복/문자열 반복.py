test_case = int(input())


for i in range(test_case):
    R, S = map(str, input().split())
    for j in range(len(S)):
        result = S[j]*int(R)
        print(result, end="")
    print("")