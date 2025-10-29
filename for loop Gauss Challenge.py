import random
import string

# Use Python's built-in string constants for cleaner character sets.
letters = string.ascii_letters  # "abc...xyzABC...XYZ"
char = "!@#$%&*"
numbers = string.digits         # "0123456789"

print(f"-------------------------\nBienvenido a PasswordGen\n-------------------------\n")

# --- Get User Input (No changes here) ---
in_letters = int(input("Escribe la cantidad de letras que quieres para tu contraseña:    "))
in_char = int(input("Escribe la cantidad de caracteres especiales que quieres para tu contraseña:    "))
in_numbers = int(input("Escribe la cantidad de numeros que quieres para tu contraseña:    "))

# --- Generate Password ---

# Use list comprehensions to generate the characters and combine them into one list.
# This is a more concise way to write the original for-loops.
password_chars = [random.choice(letters) for _ in range(in_letters)]
password_chars += [random.choice(char) for _ in range(in_char)]
password_chars += [random.choice(numbers) for _ in range(in_numbers)]

# Shuffle the list of characters to mix them up.
random.shuffle(password_chars)
# Join the list of characters back into a single string.
password = "".join(password_chars)
print(f"Tu contraseña es: {password}")


print(f"\n-------------------\nFin del programa\n-------------------\n")
