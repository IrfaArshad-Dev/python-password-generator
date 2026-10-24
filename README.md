# 🔐 Random Password Generator (Python)

A console Random Password Generator built in Python as **Project 3** of my Python Programming Internship at Decode Labs.

The user enters a password length, and the program generates a random, complex password using letters and numbers, with an option to include special characters.

## ✨ Features
- 🔢 Asks for the password length (4 to 64) and validates the input
- 🔤 Uses uppercase letters, lowercase letters and digits, plus optional special characters (`@ # $ % & * ! ?`)
- ✅ Every password always contains at least one lowercase letter, one uppercase letter, one digit (and one special character if chosen)
- 📊 Shows the password's **entropy** in bits and a strength label
- 🔁 Generate as many passwords as you like in one run

## 🧠 Concepts Practised
- **Importing modules:** `secrets`, `string`, `math`
- **`secrets.choice()`** instead of `random.choice()`: the `random` module is predictable, while `secrets` uses the operating system's secure randomness
- **String module:** `string.ascii_lowercase`, `string.ascii_uppercase`, `string.digits`
- **`"".join(list)`** to build the final string (more efficient than adding characters with `+=` in a loop)
- **Entropy:** `E = L × log2(R)`, where L is the length and R is the size of the character pool
- **Input validation** with `try / except ValueError`
- **Functions** and `if __name__ == "__main__": main()`

## ▶️ How to Run
```bash
python password_generator.py
```
Requires Python 3. No extra libraries needed.

## 📸 Example
```
===== RANDOM PASSWORD GENERATOR =====

Enter password length (4-64): 16
Include special characters (@ # $ ...)? (y/n): y

Your password: NIV!ahxh#of5!rS0
Entropy: 98 bits (Very strong)

Generate another? (y/n): n
Goodbye! Stay safe online.
```

## 💡 Note on Length
Longer is stronger. Each extra character multiplies the number of possible passwords, so a 16-character password is far harder to crack than an 8-character one.

## 🚀 Possible Next Steps
- Let the user choose which character types to include
- Copy the password to the clipboard
- Save generated passwords securely

## 👩‍💻 Author
**Irfa Arshad** | [GitHub](https://github.com/IrfaArshad-Dev)

*Built during the Decode Labs Python Programming Internship (Oct to Nov 2026).*
