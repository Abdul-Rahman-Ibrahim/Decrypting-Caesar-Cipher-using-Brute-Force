# Caesar Cipher Decryption Tool

This Python script is designed to decrypt text encrypted with a Caesar Cipher by finding the best key through word matching from a given dictionary. The script attempts all possible shifts (from 0 to 25) to determine the key that results in the most recognizable words.

## Features

- **Brute Force Decryption**: The script tries all possible Caesar Cipher shifts (0 to 25) and finds the best match based on a predefined word list.
- **Word Matching**: It uses a dictionary of words (provided in a `words.txt` file) to identify the key that produces the most recognizable English words from the encrypted text.
- **Automatic Decryption**: Once the best key is identified, the entire encrypted text is decrypted using that key.

## Requirements

- Python 3.x
- `words.txt` file: A plain text file containing a list of valid words (one word per line) that the script will use to match decrypted words.
- `encrypted_text.txt` file: The file that contains the text encrypted with a Caesar Cipher.

## Installation

1. Clone this repository to your local machine.
2. Ensure that the Python interpreter is installed on your system.
3. Place your dictionary of words in a file named `words.txt` in the same directory.
4. Place the encrypted text in a file named `encrypted_text.txt` in the same directory.

## Usage

1. Run the script by executing:

    ```bash
    python caesar_cipher.py
    ```

2. The script will automatically attempt to decrypt the file using different keys (shifts from 0 to 25).
3. Once the best key is found, the decrypted message will be displayed.

## Example

If `words.txt` contains:
hello

world

this

is

a

test


And `encrypted_text.txt` contains:
Khoor zruog!


The script will detect that the best key is `3` and will output:

Hello world!


## How it Works

1. **Initialization**: The script loads the word list from the `words.txt` file and stores it in memory. It also initializes the alphabet to be used for shifting letters.
2. **Decryption**: The script reads the encrypted text and tries all possible Caesar Cipher shifts. For each shift, it compares the decrypted words against the word list to count how many words are recognizable.
3. **Result**: The script finds the key with the highest match count and uses it to decrypt the entire text.

## Customization

- **Dictionary**: You can update the `words.txt` file with any set of words you'd like the script to use for matching.
- **Encrypted File**: Simply replace the content of `encrypted_text.txt` with any other encrypted text you want to decrypt.

## License

This project is open-source and licensed under the MIT License. Feel free to modify and distribute it.



