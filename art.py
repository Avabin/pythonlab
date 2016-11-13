temp = 0
suma = 0
while 1:
    temp = float(input("Cena> "))
    if temp == -1:
        break
    suma += temp
print(suma)
cena = suma - 0.2 * suma
print(cena)
