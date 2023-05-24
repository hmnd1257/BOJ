def get_sale_price(stamp_num, shop_price):
    sale_prices = []
    
    if stamp_num >= 5:
        sale_prices.append(500)
    if stamp_num >= 10:
        sale_prices.append(shop_price // 10)
    if stamp_num >= 15:
        sale_prices.append(2000)
    if stamp_num >= 20:
        sale_prices.append(shop_price // 4)
        
    return max(sale_prices) if sale_prices else 0
       
def attendance_event(stamp_num, shop_price):
    total_price = 0
    
    sale_price = get_sale_price(
        stamp_num=stamp_num, shop_price=shop_price
    )
    
    if shop_price - sale_price > 0:
        total_price = shop_price - sale_price
        
    return total_price
    
if __name__ == "__main__":
    stamp_num = int(input())
    shop_price = int(input())
    
    print(attendance_event(stamp_num=stamp_num, shop_price=shop_price))