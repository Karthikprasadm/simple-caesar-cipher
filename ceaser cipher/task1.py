def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher ===")
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
            continue
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (0-25): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer between 0 and 25.")
            continue
        if not (0 <= shift <= 25):
            print("Shift value out of range. Please enter a value between 0 and 25.")
            continue
        result = caesar_cipher(message, shift, mode)
        print(f"\nResult ({mode}ed): {result}\n")
        again = input("Do you want to process another message? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()