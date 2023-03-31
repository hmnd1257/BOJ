ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
arr = (cx - az, cy//ay, cz - ax)
print(arr[0], arr[1], arr[2])