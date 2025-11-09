from stats import no_of_words, get_word_count, char_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

text = get_book_text(book_path)

print("Found",get_word_count(text),"total words")

print("--------- Character Count -------")

for char in char_count(book_path):
    print(char["char"]+":",char["num"])
print("============= END ===============")


