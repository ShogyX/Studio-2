import re


def search_special_int_caps(text):
    results = {
        "special_characters": 0,
        "integers": 0,
        "capitalized_letters": 0
    }
    
    special_characters = re.findall(r'[^a-zA-Z0-9\s]', text)
    integers = re.findall(r'\d', text)
    capitalized_letters = re.findall(r'[A-Z]', text)
    
    if special_characters:
        results["special_characters"] = special_characters
    if integers:
        results["integers"] = integers
    if capitalized_letters:
        results["capitalized_letters"] = capitalized_letters
    
    return results
    