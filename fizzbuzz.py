#  FizzBuzz un variācijas
import sys

def main():
    # Pārbaude: vai ir padots arguments
    if len(sys.argv) < 2:
        print("Kļūda: jānorāda vesels skaitlis N.")
        print("Piemērs: python fizzbuzz.py 15")
        return

    # Pārbaude: vai N ir skaitlis
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Kļūda: N jābūt veselam skaitlim.")
        return

    if n < 1:
        print("Kļūda: N jābūt pozitīvam veselam skaitlim.")
        return

    for i in range(1, n + 1):
        # SVARĪGI: vispirms pārbauda dalāmību ar abiem
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
# fizzbuzz.py
import sys

def main():
    if len(sys.argv) < 2:
        print("Kļūda: jānorāda vesels skaitlis N.")
        print("Piemērs: python fizzbuzz.py 15")
        return

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Kļūda: N jābūt veselam skaitlim.")
        return

    if n < 1:
        print("Kļūda: N jābūt pozitīvam veselam skaitlim.")
        return

    # Dalītāji un atbilstošie vārdi (vari pievienot jaunus)
    rules = {
        3: "Fizz",
        5: "Buzz",
        7: "Jazz"
    }

    for i in range(1, n + 1):
        result = ""

        for divisor, word in rules.items():
            if i % divisor == 0:
                result += word

        if result:
            print(result)
        else:
            print(i)

if __name__ == "__main__":
    main()