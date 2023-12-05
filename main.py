import sys
import argparse


def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            return len(file.read())
    except FileNotFoundError:
        print(f"wc: {file_path}: No such file or directory")
        return 0


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"wc: {file_path}: No such file or directory")
        return 0


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(len(line.split()) for line in file)
    except FileNotFoundError:
        print(f"wc: {file_path}: No such file or directory")
        return 0


def count_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(len(line) for line in file)
    except FileNotFoundError:
        print(f"wc: {file_path}: No such file or directory")
        return 0


def main():
    parser = argparse.ArgumentParser(description='wc - Word Counter')
    parser.add_argument('file', nargs='?', default=None, help='File path or standard input if not specified')
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte counts')
    parser.add_argument('-l', '--lines', action='store_true', help='Print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='Print the word counts')
    parser.add_argument('-m', '--characters', action='store_true', help='Print the character counts')

    args = parser.parse_args()

    if not any(vars(args).values()):
        args.bytes, args.lines, args.words = True, True, True  # Default option if no flag is provided

    if args.file:
        if args.bytes:
            print(f"{count_bytes(args.file):>8} {args.file}")
        if args.lines:
            print(f"{count_lines(args.file):>8} {args.file}")
        if args.words:
            print(f"{count_words(args.file):>8} {args.file}")
        if args.characters:
            print(f"{count_characters(args.file):>8} {args.file}")
    else:
        # Read from standard input
        data = sys.stdin.read()
        if args.lines:
            print(f"{data.count(''):>8}")
        elif args.words:
            print(f"{len(data.split()):>8}")
        elif args.bytes:
            print(f"{len(data):>8}")
        elif args.characters:
            print(f"{len(data):>8}")


if __name__ == "__main__":
    main()