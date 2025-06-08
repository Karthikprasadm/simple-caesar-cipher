# How to Use the Caesar Cipher Program

## Installation
1. Ensure you have Python 3.x installed on your system
2. No additional packages are required
3. Simply download or clone the repository to your local machine

## Running the Program
1. Open a terminal or command prompt
2. Navigate to the project directory:
   ```bash
   cd "ceaser cipher"
   ```
3. Run the program:
   ```bash
   python task1.py
   ```

## Step-by-Step Usage Guide

### 1. Starting the Program
- The program will display a welcome message: "=== Caesar Cipher ==="
- You'll be prompted to choose between encryption and decryption

### 2. Choosing the Mode
- Type `encrypt` to encrypt a message
- Type `decrypt` to decrypt a message
- The program will validate your input and ask again if invalid

### 3. Entering Your Message
- Type your message when prompted
- The program accepts:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers
  - Special characters
  - Spaces
- Note: Only letters will be encrypted/decrypted; other characters remain unchanged

### 4. Setting the Shift Value
- Enter a number between 0 and 25
- This number determines how many positions each letter will be shifted
- Common shift values:
  - 3 (traditional Caesar cipher)
  - 13 (ROT13)
- The program will validate your input

### 5. Viewing Results
- The program will display your processed message
- The output shows:
  - The mode used (encrypted/decrypted)
  - The processed text
  - All formatting and case are preserved

### 6. Continuing or Exiting
- Choose whether to process another message
- Type `yes` to continue
- Type `no` to exit the program

## Examples

### Example 1: Encryption
```
Choose mode (encrypt/decrypt): encrypt
Enter your message: Hello, World!
Enter shift value (0-25): 3
Result (encrypted): Khoor, Zruog!
```

### Example 2: Decryption
```
Choose mode (encrypt/decrypt): decrypt
Enter your message: Khoor, Zruog!
Enter shift value (0-25): 3
Result (decrypted): Hello, World!
```

## Tips and Best Practices

### For Encryption:
1. Choose a shift value you can remember
2. Keep track of your shift value for decryption
3. Consider using the same shift value for related messages

### For Decryption:
1. Use the same shift value that was used for encryption
2. If you don't know the shift value, you can try values 1-25
3. Look for recognizable patterns in the decrypted text

### Security Considerations:
1. This is a basic cipher and not suitable for secure communications
2. Don't use this for sensitive information
3. Consider it as an educational tool only

## Troubleshooting

### Common Issues:
1. **Invalid Mode Error**
   - Solution: Type either 'encrypt' or 'decrypt' exactly as shown

2. **Invalid Shift Value**
   - Solution: Enter a number between 0 and 25

3. **Unexpected Results**
   - Check if you're using the correct shift value
   - Verify you're in the correct mode (encrypt/decrypt)
   - Ensure you're using the same shift value for encryption and decryption

## Need Help?
If you encounter any issues or have questions:
1. Review this guide
2. Check the README.md file
3. Contact the project maintainer 