# Wordlist Generator Python Script

This repository contains a Python script designed to create customizable wordlists. Wordlists are commonly used for password security testing, dictionary attacks, fuzzing, and data generation tasks.

## Features

- Generate wordlists with customizable parameters (length, charset, prefixes, suffixes, etc.)
- Save output to a file
- Supports command-line arguments for automation
- Easy to extend or integrate into larger projects

## Requirements

- Python 3.6 or later

## Usage

1. **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/yourusername/wordlist-generator.git
    cd wordlist-generator
    ```

2. **Run the script**:
    ```bash
    python wordlist_generator.py [options]
    ```

3. **Options:**
    - `-l`, `--length`: Length of words to generate (default: 8)
    - `-c`, `--charset`: Character set to use (default: lowercase letters)
    - `-p`, `--prefix`: Prefix to add to each word (optional)
    - `-s`, `--suffix`: Suffix to add to each word (optional)
    - `-o`, `--output`: Output file to save the wordlist (default: wordlist.txt)
    - `-h`, `--help`: Show help message and exit

    Example:
    ```bash
    python wordlist_generator.py --length 6 --charset abc123 --output mylist.txt
    ```

## Example

To generate a wordlist with all 4-letter combinations from the charset `abc123` and save it to `mylist.txt`:
```bash
python wordlist_generator.py -l 4 -c abc123 -o mylist.txt
```

## Notes

- Large charsets and word lengths will generate huge files. Use with caution.
- Ensure you have permission to use wordlists for security testing.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests to improve the script.

## Author

[Your Name]  
[Your Email or GitHub Profile]
