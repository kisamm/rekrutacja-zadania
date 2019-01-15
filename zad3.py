from decimal import Decimal

def ex3():
    return [Decimal(20 + x * 5) / 10 for x in range(8)]

print(ex3())