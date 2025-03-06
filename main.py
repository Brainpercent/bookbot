import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def main():
    # Check if a book path was provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the command line argument as the book path
    book_path = sys.argv[1]
    
    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)

    # Use get_num_words from stats.py to count words
    num_words = get_num_words(book_text)

    # Get character counts and sort them
    char_count = get_char_count(book_text)
    sorted_chars = sort_char_count(char_count)

    # Print results in the expected format
    print(f"Found {num_words} total words")
    
    # Print character counts in the specific format
    for item in sorted_chars:
        if item['char'] != ' ':  # Skip spaces for cleaner output
            print(f"{item['char']}: {item['count']}")

if __name__ == "__main__":
    main()