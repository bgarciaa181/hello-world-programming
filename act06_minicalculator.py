RATE_EUR_USD = 1.08

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
print("División entera:", num1 // num2)
print("Resto:", num1 % num2)
print("Potencia:", num1 ** num2)

celsius = float(input("Grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{fahrenheit:.2f} ºF")

euros = float(input("EUR: "))
usd = euros * RATE_EUR_USD
print(f"{usd:.2f} USD")