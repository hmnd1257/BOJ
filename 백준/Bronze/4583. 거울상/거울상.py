import sys
input = sys.stdin.readline

self_mirror_list = ["i", "o", "v", "w", "x"]
pair_mirror_list = ["b", "d", "b", "p", "q", "p"] 

while True:
    word = input().rstrip()
    if word == "#": break

    mirror_word = []
    for alphabet in word[::-1]: # 거울상이니까 뒤에서부터 확인
        if alphabet in self_mirror_list: 
            mirror_word.append(alphabet)
        elif alphabet in pair_mirror_list: 
            # 각자의 거울상 추가하게 함.
            mirror_word.append(pair_mirror_list[pair_mirror_list.index(alphabet) + 1])
        else: 
            print("INVALID")
            mirror_word = [] # 불가능한 문자 만나기 전에 리스트에 append된 경우 커버용으로 비워줌
            break
    if mirror_word: # 빈 배열 오는 경우 따로 출력하지 않기 위함
        print(*mirror_word, sep='')