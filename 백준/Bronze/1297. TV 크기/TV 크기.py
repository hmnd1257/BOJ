# 1297번 TV 크기
D, H, W = map(int, input().split())

a = ((D**2*H**2)/(H**2+W**2))**0.5
b = (W/H)*a

print(int(a), int(b))