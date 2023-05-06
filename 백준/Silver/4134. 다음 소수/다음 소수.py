# 4134번 다음 소수
def is_prime_(number):
    is_prime = True
    
    if number <= 1:
        is_prime = False
    else:
        for num in range(2, int(number**0.5)+1):
            if number % num == 0:
                is_prime = False
                break
    return is_prime

for i in range(int(input())):
    given_prime = int(input())
    next_prime_candidate = given_prime

    while not is_prime_(next_prime_candidate):
        next_prime_candidate += 1
    print(next_prime_candidate)