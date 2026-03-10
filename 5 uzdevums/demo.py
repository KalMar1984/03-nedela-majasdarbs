# Importējam funkcijas no citiem failiem
# utils.py un validators.py jāatrodas tajā pašā mapē

from utils import capitalize, clamp, is_prime, average, factorial
from validators import is_email, is_strong_password, is_valid_date


print("=== Utils demonstrācija ===")

# 1️⃣ capitalize funkcija (Paņem funkciju capitalize no faila utils.py)
result = capitalize("hello")
print(f"capitalize('hello') → {result}")

# 2️⃣ clamp funkcija (Paņem funkciju clamp no faila utils.py)
result = clamp(15, 0, 10)
print(f"clamp(15, 0, 10) → {result}")

# 3️⃣ is_prime funkcija (Paņem funkciju is_prime no faila utils.py)
result = is_prime(17)
print(f"is_prime(17) → {result}")

# 4️⃣ average funkcija (Paņem funkciju average no faila utils.py)
result = average([10, 20, 30])
print(f"average([10, 20, 30]) → {result}")

# 5️⃣ factorial ar kļūdas demonstrāciju (Paņem funkciju factorial no faila utils.py)
# Šeit izmantojam try/except, jo factorial(-1) izraisa kļūdu

try:
    result = factorial(-1) 
    print(f"factorial(-1) → {result}")
except ValueError as error:
    # Ja rodas kļūda, mēs to noķeram un izdrukājam
    print(f"factorial(-1) → ValueError: {error}")


print("\n=== Validators demonstrācija ===")

# 6️⃣ is_email funkcija (Paņem funkciju is_email no faila validators.py)
result = is_email("test@test.lv")
print(f"is_email('test@test.lv') → {result}")

# 7️⃣ is_strong_password funkcija (Paņem funkciju is_strong_password no faila validators.py)
result = is_strong_password("abc")
print(f"is_strong_password('abc') → {result}")

# 8️⃣ is_valid_date funkcija (Paņem funkciju is_valid_date no faila validators.py)
result = is_valid_date("2025-13-01")
print(f"is_valid_date('2025-13-01') → {result}")