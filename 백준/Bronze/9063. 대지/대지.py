def max_min_value(coordinate):
    x_max, x_min = coordinate[0][0], coordinate[0][0]
    y_max, y_min = coordinate[0][1], coordinate[0][1]

    for data in coordinate:
        if x_max < data[0]:
            x_max = data[0]
        if x_min > data[0]:
            x_min = data[0]
        if y_max < data[1]:
            y_max = data[1]
        if y_min > data[1]:
            y_min = data[1]

    return x_max, x_min, y_max, y_min

def calculate(x_max, x_min, y_max, y_min):
    return (x_max-x_min)*(y_max-y_min)

N = int(input())
coordinate=[]
for i in range(N):
    x, y = map(int, input().split())
    coordinate.append([x,y])

x_max, x_min, y_max, y_min = max_min_value(coordinate)
answer = calculate(x_max, x_min, y_max, y_min)
print(answer)