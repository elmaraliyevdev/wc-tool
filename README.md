# wc - Word Counter

A simple command-line tool inspired by the Unix `wc` command. It provides word count, line count, byte count, and character count functionalities. Users can use it with various options to analyze text data in files or from standard input.

## Features

- Count bytes, lines, words, and characters in a file.
- Supports options: `-c` (bytes), `-l` (lines), `-w` (words), `-m` (characters).
- Default behavior equivalent to `-c -l -w`.
- Can read from standard input if no filename is specified.

## Installation

Clone the repository:
```bash
git clone https://github.com/elmaraliyevdev/wc-tool.git
```
Navigate to the project directory:
```bash
cd wc-tool
```
Make the script executable:
```bash
chmod +x main.py
```
Move the script to a directory in your PATH (e.g., /usr/local/bin/):
```bash
sudo mv main.py /usr/local/bin/wc
```


## Usage

```bash
# Count bytes in a file
wc -c test.txt

# Count lines in a file
wc -l test.txt

# Count words in a file
wc -w test.txt

# Count characters in a file
wc -m test.txt

# Default behavior (equivalent to -c -l -w)
wc test.txt

# Read from standard input
cat test.txt | wc -l
