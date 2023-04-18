card_cnt, card_value = int(input()), set(map(int, input().split()))
check_cnt, check_value = int(input()), list(map(int, input().split()))
   
print(" ".join(str(1 if x in card_value else 0) for x in check_value))