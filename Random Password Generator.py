import random
import string

while True:
    length = input("\nEnter password length (or type 'exit' to quit): ").strip().lower()
    
    if length == "exit":
        print("Goodbye!")
        break
    
    if length.isdigit() and int(length) >= 4:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(length)))
        print("🔒 Your Random Password:", password)
    else:
        print("Please enter a valid number (minimum length: 4).")

input("\nPress Enter to exit...")
