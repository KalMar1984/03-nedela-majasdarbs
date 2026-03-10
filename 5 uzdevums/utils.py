"""
Utilītu bibliotēka ar virkņu, skaitļu un sarakstu funkcijām.

Visas funkcijas ir "tīras" (pure) – tās neizmanto print() un nerada blakusefektus.
Katra funkcija validē ievades datus.
"""


# =========================
# Virkņu funkcijas
# ========================= 

def capitalize(text):
    """Padara virknes pirmo burtu lielo.

    Args:
        text (str): ievades teksts

    Returns:
        str: teksts ar lielo sākumburtu

    Raises:
        TypeError: ja text nav str

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise TypeError("text jābūt virknei (str)")
    if not text:
        return text
    return text[0].upper() + text[1:]


def truncate(text, max_len=20):
    """Saīsina tekstu līdz max_len un pievieno '...', ja nepieciešams.

    Args:
        text (str): ievades teksts
        max_len (int, optional): maksimālais garums (noklusējums 20)

    Returns:
        str: saīsinātais teksts

    Raises:
        TypeError: ja text nav str vai max_len nav int
        ValueError: ja max_len < 0

    Example:
        >>> truncate("Sveika pasaule", 6)
        'Sveika...'
    """
    if not isinstance(text, str):
        raise TypeError("text jābūt virknei (str)")
    if not isinstance(max_len, int):
        raise TypeError("max_len jābūt veselam skaitlim")
    if max_len < 0:
        raise ValueError("max_len jābūt >= 0")

    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."


def count_words(text):
    """Saskaita vārdus tekstā.

    Args:
        text (str): ievades teksts

    Returns:
        int: vārdu skaits

    Raises:
        TypeError: ja text nav str

    Example:
        >>> count_words("Sveika mana pasaule")
        3
    """
    if not isinstance(text, str):
        raise TypeError("text jābūt virknei (str)")
    words = text.split()
    return len(words)


# =========================
# Skaitļu funkcijas
# =========================

def clamp(num, low, high):
    """Ierobežo skaitli norādītajā diapazonā.

    Args:
        num (int | float): skaitlis, ko ierobežot
        low (int | float): minimālā robeža
        high (int | float): maksimālā robeža

    Returns:
        int vai float: ierobežotā vērtība

    Raises:
        TypeError: ja parametri nav skaitļi
        ValueError: ja low > high

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    for value in (num, low, high):
        if not isinstance(value, (int, float)):
            raise TypeError("Visiem parametriem jābūt skaitļiem")

    if low > high:
        raise ValueError("low nedrīkst būt lielāks par high")

    return max(low, min(num, high))


def is_prime(num):
    """Nosaka, vai skaitlis ir pirmskaitlis.

    Args:
        num (int): pārbaudāmais skaitlis

    Returns:
        bool: True, ja ir pirmskaitlis, citādi False

    Raises:
        TypeError: ja num nav int

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
    """
    if not isinstance(num, int):
        raise TypeError("num jābūt veselam skaitlim")

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def factorial(n):
    """Aprēķina n! (faktoriālu).

    Args:
        n (int): vesels skaitlis, n >= 0

    Returns:
        int: n faktoriāls

    Raises:
        TypeError: ja n nav int
        ValueError: ja n < 0

    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("n jābūt veselam skaitlim")
    if n < 0:
        raise ValueError("n jābūt >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# =========================
# Sarakstu funkcijas
# =========================

def total(numbers):
    """Aprēķina saraksta elementu summu (izmantojot for ciklu).

    Args:
        numbers (list): saraksts ar skaitļiem

    Returns:
        int vai float: visu elementu summa

    Raises:
        TypeError: ja numbers nav saraksts vai satur neskaitliskas vērtības

    Example:
        >>> total([1, 2, 3])
        6
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers jābūt sarakstam")

    result = 0
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("Visiem elementiem jābūt skaitļiem")
        result += n
    return result


def average(numbers):
    """Aprēķina saraksta vidējo aritmētisko.

    Args:
        numbers (list): saraksts ar skaitļiem

    Returns:
        float: vidējais aritmētiskais

    Raises:
        TypeError: ja numbers nav saraksts vai satur neskaitliskas vērtības
        ValueError: ja saraksts ir tukšs

    Example:
        >>> average([2, 4, 6])
        4.0
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers jābūt sarakstam")
    if len(numbers) == 0:
        raise ValueError("Saraksts nedrīkst būt tukšs")

    return total(numbers) / len(numbers)


# =========================
# Demonstrācija
# =========================

if __name__ == "__main__":
    print("Demonstrācija:")
    print(capitalize("hello"))
    print(truncate("Šis ir ļoti garš teksts piemēram", 10))
    print(count_words("Sveika mana skaistā pasaule"))

    print(clamp(15, 0, 10))
    print(is_prime(13))
    print(factorial(5))

    print(total([1, 2, 3, 4]))
    print(average([10, 20, 30]))