import re

password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1

# Number Check
if re.search(r"[0-9]", password):
    score += 1

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nPassword Analysis")
print("-" * 30)

print("Length:", len(password))

if score <= 2:
    print("Strength: WEAK")
elif score <= 4:
    print("Strength: MEDIUM")
else:
    print("Strength: STRONG")

print("\nChecks:")

print("✓ Minimum 8 Characters" if len(password) >= 8 else "✗ Minimum 8 Characters")
print("✓ Uppercase Letter" if re.search(r"[A-Z]", password) else "✗ Uppercase Letter")
print("✓ Lowercase Letter" if re.search(r"[a-z]", password) else "✗ Lowercase Letter")
print("✓ Number" if re.search(r"[0-9]", password) else "✗ Number")
print("✓ Special Character" if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else "✗ Special Character")