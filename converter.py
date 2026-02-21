# Konversijas konstantes
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

print("=== Vienību konvertors ===")
print("1 - Kilometri → Jūdzes")
print("2 - Jūdzes → Kilometri")
print("3 - Kilogrami → Mārciņas")
print("4 - Mārciņas → Kilogrami")
print("5 - Litri → Galoni")
print("6 - Galoni → Litri")
print("7 - Dolāri → Eiro")
print("8 - Eiro → Dolāri")

izvele = input("Izvēlies konversijas veidu (1-8): ")

try:
    vertiba = float(input("Ievadi vērtību konvertēšanai: "))

    if izvele == "1":
        rezultats = vertiba * KM_TO_MI
        print(f"{vertiba:.2f} km = {rezultats:.2f} mi")

    elif izvele == "2":
        rezultats = vertiba / KM_TO_MI
        print(f"{vertiba:.2f} mi = {rezultats:.2f} km")

    elif izvele == "3":
        rezultats = vertiba * KG_TO_LB
        print(f"{vertiba:.2f} kg = {rezultats:.2f} lb")

    elif izvele == "4":
        rezultats = vertiba / KG_TO_LB
        print(f"{vertiba:.2f} lb = {rezultats:.2f} kg")

    elif izvele == "5":
        rezultats = vertiba * L_TO_GAL
        print(f"{vertiba:.2f} L = {rezultats:.2f} gal")

    elif izvele == "6":
        rezultats = vertiba / L_TO_GAL
        print(f"{vertiba:.2f} gal = {rezultats:.2f} L")

    elif izvele == "7":
        rezultats = vertiba * USD_TO_EUR
        print(f"{vertiba:.2f} $ = {rezultats:.2f} €")

    elif izvele == "8":
        rezultats = vertiba / USD_TO_EUR
        print(f"{vertiba:.2f} € = {rezultats:.2f} $")

    else:
        print("Nepareiza izvēle! Lūdzu izvēlies skaitli no 1 līdz 8.")

except ValueError:
    print("Kļūda: Ievadītā vērtība nav derīgs skaitlis!")