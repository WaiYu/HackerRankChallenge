T = int(raw_input())
for i in range (0,T):
    money,price,exchange = [int(x) for x in raw_input().split(' ')]
    
    total_choco = money/price
    wrapper = total_choco
    while wrapper >= exchange:
        total_choco += wrapper / exchange
        wrapper = wrapper / exchange + wrapper % exchange
    print total_choco
