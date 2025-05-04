from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f :
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book = get_book_text(sys.argv[1])
    count = word_counter(book)
    num_dic = char_count(book)
    sortd = get_sorted(num_dic)
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {sys.argv[1]} \n" 
    "----------- Word Count ----------\n" 
    f"Found {count} total words\n"
        "--------- Character Count -------\n",
        )
    for di in sortd:
        print(f"{di["char"]}: {di["num"]}")
    print("============= END ===============")

main()