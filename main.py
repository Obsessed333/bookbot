import sys
from stats import get_num_words, get_num_char, sorted_list


if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"- Found {num_words} total words")
    num_char = get_num_char(text)
    sus = sorted_list(num_char)
    for value in sus:
        char = value["char"]
        num = value["num"]
        print(f"{char}: {num}")

if __name__ == "__main__":
    main()



