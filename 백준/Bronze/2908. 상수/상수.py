A, B = map(str, input().split())

A_list = list(A)
B_list = list(B)

A_list.reverse()
B_list.reverse()

A_rev = ''.join(A_list)
B_rev = ''.join(B_list)
if A_rev > B_rev:
    print(A_rev)
else:
    print(B_rev)