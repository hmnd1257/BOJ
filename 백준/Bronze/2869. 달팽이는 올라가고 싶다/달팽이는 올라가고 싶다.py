# 2869번 달팽이는 올라가고 싶다
import math

up, down, h = map(int, input().split())

result = (h-down)/(up-down)
print(math.ceil(result))