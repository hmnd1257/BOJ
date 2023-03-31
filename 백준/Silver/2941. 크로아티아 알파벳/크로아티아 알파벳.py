alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = str(input())

for i in alpha:
    word = word.replace(i,'x')
print(len(word))