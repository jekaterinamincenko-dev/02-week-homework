# Minēšanas spēle
import random

while True:  # ārējais cikls - lai var spēlēt atkārtoti
    slepenais_skaitlis = random.randint(1, 100)
    megjinajumi = 0
    max_megjinajumi = 10

    print("\nTiek iedomāts skaitlis no 1 līdz 100.")
    print("Tev ir 10 mēģinājumi to uzminēt!")

    while True:  # iekšējais cikls minēšanai
        minejums = input("Tavs minējums: ")

        # Pārbaude vai ievade ir skaitlis
        try:
            minejums = int(minejums)
        except ValueError:
            print("Lūdzu ievadi veselu skaitli!")
            continue  # turpina ciklu, nepārtrauc spēli

        megjinajumi += 1

        if minejums > slepenais_skaitlis:
            print("Par lielu!")
        elif minejums < slepenais_skaitlis:
            print("Par mazu!")
        else:
            print("Apsveicu! Tu uzminēji skaitli!")
            break  # iziet no minēšanas cikla

        if megjinajumi >= max_megjinajumi:
            print("Beigušies mēģinājumi!")
            break  # iziet, ja sasniegti 10 mēģinājumi

    print(f"Tu izmantoji {megjinajumi} mēģinājumus.")
    print(f"Pareizais skaitlis bija: {slepenais_skaitlis}")

    # Piedāvājums spēlēt vēlreiz
    velreiz = input("Vai vēlies spēlēt vēlreiz? (j/n): ").lower()
    if velreiz != "j":
        print("Paldies par spēli!")
        break