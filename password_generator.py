
import math
import secrets   # secure random choices (better than the random module for passwords)
import string    # ready-made character sets

MIN_LENGTH = 4
MAX_LENGTH = 64


def ask_length():
    """Keep asking until the user enters a valid whole number."""
    while True:
        entry = input(f"Enter password length ({MIN_LENGTH}-{MAX_LENGTH}): ").strip()
        try:
            length = int(entry)
        except ValueError:
            print("Invalid input. Please enter a whole number, e.g. 12.\n")
            continue
        if length < MIN_LENGTH or length > MAX_LENGTH:
            print(f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}.\n")
            continue
        return length


def generate_password(length, use_symbols):
    """Build a random password of the given length."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "@#$%&*!?"

    pool = lower + upper + digits          # all characters we can pick from
    if use_symbols:
        pool = pool + symbols

    # Make sure the password has at least one of each type
    chars = [secrets.choice(lower), secrets.choice(upper), secrets.choice(digits)]
    if use_symbols:
        chars.append(secrets.choice(symbols))

    # Fill the remaining length with random characters from the pool
    while len(chars) < length:
        chars.append(secrets.choice(pool))

    # Shuffle so the guaranteed characters are not always at the start
    secrets.SystemRandom().shuffle(chars)

    return "".join(chars), len(pool)       # join() is faster than += in a loop


def strength(entropy_bits):
    if entropy_bits < 50:
        return "Weak"
    if entropy_bits < 70:
        return "Fair"
    if entropy_bits < 90:
        return "Strong"
    return "Very strong"


def main():
    print("===== RANDOM PASSWORD GENERATOR =====\n")

    while True:
        length = ask_length()
        answer = input("Include special characters (@ # $ ...)? (y/n): ").strip().lower()
        use_symbols = (answer == "y")

        password, pool_size = generate_password(length, use_symbols)
        entropy = length * math.log2(pool_size)    # E = L x log2(R)

        print(f"\nYour password: {password}")
        print(f"Entropy: {entropy:.0f} bits ({strength(entropy)})")
        if length < 12:
            print("Tip: 12 or more characters is much safer.")

        again = input("\nGenerate another? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Stay safe online.")
            break
        print()


if __name__ == "__main__":
    main()