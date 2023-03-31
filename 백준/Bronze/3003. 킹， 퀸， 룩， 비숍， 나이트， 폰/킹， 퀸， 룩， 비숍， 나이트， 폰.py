# 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰

chees_li = [1, 1, 2, 2, 2, 8]

king, queen, rook, bishop, knight, pawn = map(int, input().split())
num_li = [king, queen, rook, bishop, knight, pawn]

for i in range(len(chees_li)):
    result = chees_li[i] - num_li[i]
    print(result, end=' ')