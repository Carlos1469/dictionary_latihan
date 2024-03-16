angka_minimum = int(input("Masukkan angka minimum: "))
angka_maximum = int(input("Masukkan angka maksimum: "))

primas = {1}
komposits = {}

for number in range(angka_minimum, angka_maximum + 1):
    if number > 1:
        is_prima = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prima = False
        if is_prima:
            primas[number] = "Prima"
        else:
            komposits[number] = "komposit"

print("Bilangan Prima:")
for prima in primas.keys():
    print(prima, end=", ")

print("\nBilangan Komposit:")
for komposit in komposits.keys():
    print(komposit, end=", ")