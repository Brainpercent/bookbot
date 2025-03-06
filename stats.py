def get_num_words(text):
    """
    Count the number of words in the given text.
    
    Args:
        text (str): Input text to count words from
    
    Returns:
        int: Total number of words in the text
    """
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Count occurrences of each character in the text, converting all characters to lowercase.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary mapping each character to its count
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Count each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_char_count(char_count_dict):
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "count": count})
    
    # Sort the list by count in descending order
    char_list.sort(key=lambda x: x["count"], reverse=True)
    
    return char_list