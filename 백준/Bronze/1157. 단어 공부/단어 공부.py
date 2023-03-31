alp = str(input()).upper()
alp_list = list(set(alp))

cnt = []
for i in alp_list:
    a = alp.count(i)
    cnt.append(a)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(alp_list[(cnt.index(max(cnt)))].upper())