from act04_config import BASE_PRICE, IVA, DISCOUNT, CURRENCY

total = BASE_PRICE * IVA
final = total - (total * DISCOUNT)

print("Precio final:", final, CURRENCY)