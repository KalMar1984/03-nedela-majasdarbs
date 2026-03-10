"""
game_logic.py
Satur spēles loģikas funkcijas.
Šeit NAV ievades vai izvades (print/input).
"""

import random


def generate_secret(low=1, high=100):
    """
    Ģenerē un atgriež nejaušu skaitli dotajā diapazonā.
    """
    return random.randint(low, high)


def check_guess(guess, secret):
    """
    Salīdzina spēlētāja minējumu ar slepeno skaitli.
    
    Atgriež:
    - "correct" ja uzminēts
    - "too_low" ja minējums par mazu
    - "too_high" ja minējums par lielu
    """
    if guess < secret:
        return "too_low"
    elif guess > secret:
        return "too_high"
    else:
        return "correct"


def is_game_over(attempts, max_attempts=10):
    """
    Pārbauda vai spēle ir beigusies pēc mēģinājumu skaita.
    """
    return attempts >= max_attempts


if __name__ == "__main__":
    # Vienkāršs tests
    secret = generate_secret()
    print("Testa slepenais skaitlis:", secret)
    print("Testa pārbaude:", check_guess(50, secret))