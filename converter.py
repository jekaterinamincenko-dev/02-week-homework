# Vienību konvertors
def km_to_miles(km):
    return km*0.621371
def miles_to_km(miles):
    return miles/0.621371
def kg_to_pounds(kg):
    return kg * 2.20462
def pounds_to_kg(pounds):
    return pounds / 2.20462
def liters_to_gallons(liters):
    return liters * 0.264172
def gallons_to_liters(gallons):
    return gallons / 0.264172
def usd_to_eur(usd):
    return usd * 0.84235020
def eur_to_usd(eur):
    return eur / 0.84235020

def main():
    print("=== VIENĪBU KONVERTORS ===")
    print("1 - Kilometers ↔ Miles")
    print("2 - Kilograms ↔ Pounds")
    print("3 - Liters ↔ Gallons")
    print("4 - USD ↔ EUR")
    choice = input("Choose conversion type (1-4): ")
    try:
        value = float(input("Enter value to convert: "))
    except ValueError:
        print("Invalid number!")
        return
    
    if choice == "1":
        direction = input("Type 'km' to convert KM→Miles or 'mi' for Miles→KM: ")
        if direction == "km":
            print("Result:", km_to_miles(value), "miles")
        elif direction == "mi":
            print("Result:", miles_to_km(value), "km")
        else:
            print("Invalid direction!")

    elif choice == "2":
        direction = input("Type 'kg' to convert KG→Pounds or 'lb' for Pounds→KG: ")
        if direction == "kg":
            print("Result:", kg_to_pounds(value), "pounds")
        elif direction == "lb":
            print("Result:", pounds_to_kg(value), "kg")
        else:
            print("Invalid direction!")

    elif choice == "3":
        direction = input("Type 'L' to convert L→Gallons or 'gal' for Gallons→L: ")
        if direction.lower() == "l":
            print("Result:", liters_to_gallons(value), "gallons")
        elif direction.lower() == "gal":
            print("Result:", gallons_to_liters(value), "liters")
        else:
            print("Invalid direction!")  

    elif choice == "4":
        direction = input("Type 'usd' to convert USD→EUR or 'eur' for EUR→USD: ")
        if direction.lower() == "usd":
            print("Result:", usd_to_eur(value), "EUR")
        elif direction.lower() == "eur":
            print("Result:", eur_to_usd(value), "USD")
        else:
            print("Invalid direction!")      
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()