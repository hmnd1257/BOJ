# 1181번 단어 정렬
# sort함수에 key 파라미터로 길이 순으로 정렬가능!!
N = int(input())

word_li = []
for i in range(N):
    word = str(input())
    word_li.append((len(word), word))

word_li = list(set(word_li))

word_li = sorted(word_li, key=lambda x: (x[0],x[1]))
for _, word in word_li:
    print(word)