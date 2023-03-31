li = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    word = str(input())
    if word == '#':
        break
        
    word = word.lower()
    for i in word:
        if i in li:
            cnt += 1
    print(cnt)