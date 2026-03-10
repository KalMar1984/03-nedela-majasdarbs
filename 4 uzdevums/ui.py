"""
ui.py
Satur lietotāja ievades un izvades funkcijas.
"""

from validators import validate_number


def get_player_guess():
    """
    Pieprasa spēlētāja minējumu.
    Atgriež int vai None, ja ievade nav korekta.
    """
    user_input = input("Tavs minējums: ")
    number = validate_number(user_input)

    if number is None:
        print("Lūdzu ievadi skaitli!")
        return None

    return number


def show_hint(result):
    """
    Parāda padomu, balstoties uz rezultātu.
    """
    if result == "too_low":
        print("Par mazu")
    elif result == "too_high":
        print("Par lielu")
    elif result == "correct":
        print("Pareizi!")


def show_game_over(secret, attempts, won):
    """
    Parāda spēles beigu ziņojumu.
    """
    if not won:
        print("Beidzās mēģinājumi.")

    print(f"Mēģinājumi: {attempts}")
    print(f"Pareizais skaitlis bija: {secret}")


def ask_play_again():
    """
    Pajautā vai spēlēt vēlreiz.
    Atgriež True vai False.
    """
    again = input("Spēlēt vēlreiz? (j/n): ").lower()
    return again == "j"


if __name__ == "__main__":
    guess = get_player_guess()
    print("Ievadītais:", guess)