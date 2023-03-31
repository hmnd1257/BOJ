from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
S = input()

for i in alpha_list:
    print(S.find(i), end =" ")