# Caesar Cipher Implementation

## Overview
This project implements the classic Caesar Cipher, one of the oldest and simplest encryption techniques. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet.

## Features
- Encrypt and decrypt text messages
- Support for both uppercase and lowercase letters
- Preservation of non-alphabetic characters
- Interactive command-line interface
- Shift value validation (0-25)
- Case-sensitive encryption/decryption

## Technical Details
- Written in Python 3
- No external dependencies required
- Implements modular arithmetic for circular alphabet shifting
- Handles edge cases and input validation

## How It Works
The Caesar Cipher works by shifting each letter in the alphabet by a fixed number of positions. For example, with a shift of 3:
- A becomes D
- B becomes E
- C becomes F
- ... and so on

The formula used is:
- Encryption: (original_position + shift) mod 26
- Decryption: (original_position - shift) mod 26

## Security Note
While the Caesar Cipher is a great educational tool, it is not secure for modern cryptographic needs. It can be easily broken through:
- Brute force (only 25 possible keys)
- Frequency analysis
- Known plaintext attacks

## Project Structure
```
.
├── HOW_TO_USE.md     # Detailed usage instructions
├── README.md         # Project documentation (this file)
├── ceaser cipher/
│   └── task1.py      # Main implementation file
└── LICENSE           # License file
```

## Requirements
- Python 3.x
- No additional packages required

## Branch Information
- The default branch is now `main`.
- All files, including documentation, are at the root or in their respective folders.

## License
This project is open source and available for educational purposes.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

## Author
[Your Name]

## Acknowledgments
- The Caesar Cipher is named after Julius Caesar, who used it in his private correspondence
- This implementation is based on the classical version of the cipher 