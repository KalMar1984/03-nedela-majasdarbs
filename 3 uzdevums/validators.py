"""
validators.py

Šis ir modulis (Python fails), kurā glabājas vairākas validācijas funkcijas.
Validācija nozīmē datu pārbaudi — vai ievadītā informācija atbilst noteiktiem noteikumiem.

Katras funkcijas uzdevums ir atgriezt:
True  -> ja dati ir pareizi 
False -> ja dati nav pareizi
"""

# ---------------------------------------------------------
# 1. E-PASTA VALIDĀCIJA
# ---------------------------------------------------------

def is_email(text):
    """
    Pārbauda, vai teksts izskatās pēc vienkārša e-pasta.
    
    Nosacījumi:
    - satur simbolu '@'
    - satur punktu '.'
    - '@' nav pirmais vai pēdējais simbols
    """
    
    # Pārbaudām vai tekstā ir '@'
    if "@" not in text:
        return False  # ja nav, tad e-pasts nav derīgs
    
    # Pārbaudām vai tekstā ir '.'
    if "." not in text:
        return False  # ja nav punkta, nav derīgs
    
    # Pārbaudām vai '@' nav pirmais simbols
    if text.startswith("@"):
        return False
    
    # Pārbaudām vai '@' nav pēdējais simbols
    if text.endswith("@"):
        return False
    
    # Ja visi nosacījumi izpildīti
    return True


# ---------------------------------------------------------
# 2. TELEFONA NUMURA VALIDĀCIJA
# ---------------------------------------------------------

def is_phone_number(text):
    """
    Pārbauda vai telefona numurs atbilst Latvijas formātam:
    +371 XXXXXXXX
    
    Nosacījumi:
    - sākas ar '+371 '
    - pēc atstarpes seko tieši 8 cipari
    """
    
    # Pārbaudām vai teksts sākas ar pareizo valsts kodu
    if not text.startswith("+371 "):
        return False
    
    # Izņemam daļu pēc '+371 '
    number_part = text[5:]  # [5:] nozīmē: sākot no 5. pozīcijas līdz beigām
    
    # Pārbaudām vai ir tieši 8 simboli
    if len(number_part) != 8:
        return False
    
    # Pārbaudām vai visi simboli ir cipari
    if not number_part.isdigit():
        return False
    
    return True


# ---------------------------------------------------------
# 3. VECUMA VALIDĀCIJA
# ---------------------------------------------------------

def is_valid_age(age):
    """
    Pārbauda vai vecums:
    - ir vesels skaitlis (int)
    - ir robežās no 0 līdz 150
    """
    
    # Pārbaudām vai tips ir int (vesels skaitlis)
    if not isinstance(age, int):
        return False
    
    # Pārbaudām vai vecums ir atļautajā diapazonā
    if age < 0 or age > 150:
        return False
    
    return True


# ---------------------------------------------------------
# 4. PAROLES STIPRUMA VALIDĀCIJA
# ---------------------------------------------------------

def is_strong_password(text):
    """
    Pārbauda vai parole:
    - ir vismaz 8 simbolus gara
    - satur vismaz vienu burtu
    - satur vismaz vienu ciparu
    """
    
    # Pārbaudām garumu
    if len(text) < 8:
        return False
    
    # Mainīgie, kuros glabāsim informāciju
    has_letter = False
    has_digit = False
    
    # Pārbaudām katru simbolu
    for char in text:
        if char.isalpha():  # vai ir burts
            has_letter = True
        if char.isdigit():  # vai ir cipars
            has_digit = True
    
    # Atgriež True tikai tad, ja abi nosacījumi izpildīti
    return has_letter and has_digit


# ---------------------------------------------------------
# 5. DATUMA VALIDĀCIJA
# ---------------------------------------------------------

def is_valid_date(text):
    """
    Pārbauda vai datums ir formātā:
    YYYY-MM-DD
    
    Vienkārša pārbaude:
    - garums 10 simboli
    - 4 cipari, '-', 2 cipari, '-', 2 cipari
    """
    
    # Garuma pārbaude
    if len(text) != 10:
        return False
    
    # Pārbaudām vai 5. un 8. simbols ir '-'
    if text[4] != "-" or text[7] != "-":
        return False
    
    # Izdalām daļas
    year = text[0:4]
    month = text[5:7]
    day = text[8:10]
    
    # Pārbaudām vai tās ir tikai cipari
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    
    return True


# ---------------------------------------------------------
# TESTĒŠANAS BLOKS
# ---------------------------------------------------------

# Šis kods izpildās TIKAI tad, ja fails tiek palaists tieši,
# nevis importēts citā failā.
if __name__ == "__main__":
    
    print("=== EMAIL TESTI ===")
    print(is_email("anna@inbox.lv"))   # True
    print(is_email("anna"))            # False
    print(is_email("anna@"))           # False
    
    print("\n=== TELEFONS TESTI ===")
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))       # False
    print(is_phone_number("+371 123"))       # False
    
    print("\n=== VECUMS TESTI ===")
    print(is_valid_age(25))     # True
    print(is_valid_age(-1))     # False
    print(is_valid_age(200))    # False
    
    print("\n=== PAROLE TESTI ===")
    print(is_strong_password("abc12345"))  # True
    print(is_strong_password("abcdefg"))   # False
    print(is_strong_password("12345678"))  # False
    
    print("\n=== DATUMS TESTI ===")
    print(is_valid_date("2024-05-20"))  # True
    print(is_valid_date("2024/05/20"))  # False
    print(is_valid_date("20-05-2024"))  # False