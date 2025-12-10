import sys
from stats import get_num_words, character_count, sort_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path= sys.argv[1]
    text = get_book_text(file_path)
    char_count = character_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    sort_list(char_count)
    print("============= END ===============")
main()
