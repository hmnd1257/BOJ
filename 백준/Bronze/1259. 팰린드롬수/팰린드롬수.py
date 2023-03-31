# 1259번 팰린드롬수

while True:
    word = str(input())
    if word == '0':
        break
    
    if word == word[::-1]:
        print("yes")
    else:
        print("no")