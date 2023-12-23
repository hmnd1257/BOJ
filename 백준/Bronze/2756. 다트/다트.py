from sys import stdin

test_case = int(stdin.readline())

for test_case_idx in range(test_case):
    floats = list(map(float, stdin.readline().split(' ')))
    N = 0
    M = 0
    winner = None

    for idx in range(0, 12, 2):
        point = 0
        distance = floats[idx] ** 2 + floats[idx+1] ** 2

        if distance <= 9:
            point += 100
        elif 9 < distance <= 36:
            point += 80
        elif 36 < distance <= 81:
            point += 60
        elif 81 < distance <= 144:
            point += 40
        elif 144 < distance <= 225:
            point += 20
        if 0 <= idx <= 4:
            N += point
        else:
            M += point

    if N > M:
        winner = "PLAYER 1 WINS"
    elif N < M:
        winner = "PLAYER 2 WINS"
    else:
        winner = "TIE"

    print(f'SCORE: {N} to {M}, {winner}.')