#  2 pamata tipi vērtības mainīgajiem
# str (teksts)
name = "Jekaterina"
surname = "Minčenko"
print(type(surname))
# int (veseli skaitļi)
age = 33
amount = 2
print(type(age))
# float (decimālskaitļi)
x = 1.59
y = 2003.5
print(type(y))
# bool (loģiskās vērtības)
i_am_woman = True
i_am_man = False
print(type(i_am_man))
# None (nav vērtības)
time = None
code = None
print(type(code))
# Konsoles izvade
print("name:", type(name))
print("age:", type(age))
print("x:", type(x))
print("i_am_woman:", type(i_am_woman))
print("time:", type(time))
# Vismaz 3 Python truthy/falsy uzvedības piemērus ar komentāriem
print(bool(0.0))   # False
print(bool(0.5))   # True (Nav tukšs)
print(bool(""))    # False (Nav vērtības)
print(bool("Good_morning"))  # True (Ir vērtība)
name = ""
if name:
    print("name")
else:
    print("None") # izpildās
numbers = [1, 2, 3]
if numbers:
    print("List is not empty")  #izpildās
# Tiešās datu tipu pārveides ar robežgadījumiem:
# String to list
print(list("ABC"))  #['A', 'B', 'C'] Veiksmīga konversija
try:
    print(list(123))
except TypeError as e:
    print("Conversion failed:", e)  # robežgadījums: vesela skaitļa konvertēšana
# Float to int (robežgadījums) 
print(int(5.8))  # 5; decimāldaļa nogriezta
print(int(-5.8))  # -5; nevis 6
# String to int
print(int("123")) # 123; veiksmīga konversija
try:
    print(int("QN12B"))
except ValueError as e:
    print("Conversion failed:", e)  #robežgadījums: nepareizs skaitlis