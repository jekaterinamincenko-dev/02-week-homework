# Atbilstības pārbaudītājs 
def parse_yes_no(answer):
    """Pārvērš j/n ievadi par bool vērtību."""
    answer = answer.strip().lower()
    if answer == "j":
        return True
    elif answer == "n":
        return False
    else:
        raise ValueError("Ievadei jābūt 'j' vai 'n'.")

try:
    age_input = input("Ievadi vecumu: ").strip()
    age = int(age_input)

    if age < 0:
        raise ValueError("Vecums nevar būt negatīvs.")

    has_license = parse_yes_no(input("Vai ir autovadītāja apliecība? (j/n): "))
    is_student = parse_yes_no(input("Vai ir students? (j/n): "))
    is_veteran = parse_yes_no(input("Vai ir veterāns? (j/n): "))

except ValueError as e:
    print(f"Kļūda: {e}")
    exit()

# --- Atbilstības nosacījumi ---

can_vote = age >= 18
can_rent = age >= 21 and has_license
senior_discount = age >= 65 or is_veteran
student_discount = 16 <= age <= 26 and is_student

# --- Rezultātu formatēšana ---

vote_result = "Jā ✓" if can_vote else "Nē ✗"
rent_result = (
    "Jā ✓"
    if can_rent
    else "Nē ✗ (nav apliecības)" if age >= 21 and not has_license
    else "Nē ✗ (par jaunu)"
)
senior_result = "Jā ✓" if senior_discount else "Nē ✗"
student_result = "Jā ✓" if student_discount else "Nē ✗"

# --- Izvade ---

print("\n---")
print(f"Balsošana:         {vote_result}")
print(f"Auto īre:          {rent_result}")
print(f"Senioru atlaide:   {senior_result}")
print(f"Studentu atlaide:  {student_result}")