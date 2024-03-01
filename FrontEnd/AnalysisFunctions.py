import re
import wordsegment
#The standard way of structuring information to be passed to the front end is to place it into a dict and import the function into the app.py file 
#And call it inside the analyze_password(password) function. This call then be unpacked and combined with the final dict.

#Returns the amount of Sepcial Characters, Integers And Capital Letters
def search_special_int_caps(string):
    # Dict where the count of each occurence will be stored
    counts = {}

    # Iterate through each character in the string and search for the values specified.
    for char in string:
        if char.isalpha() and char.isupper():
            counts['capital_letters'] = counts.get('capital_letters', 0) + 1
        elif char.isdigit():
            counts['integers'] = counts.get('integers', 0) + 1
        elif not char.isalnum():
            counts['special_characters'] = counts.get('special_characters', 0) + 1

    # This checks the counts dict if any value was found. Basically makes sure that the function does not return anything unless somethign was found.
    result = {k: v for k, v in counts.items() if v > 0}
    #returns the resulting dict. will be empty if nothing is found.
    return result

print(search_special_int_caps("HElloWorld12345!!"))

def detect_words(input_string):

    cleaned = re.sub(r'[^a-zA-Z]', '', input_string) #remove any non letter characters
    wordsegment.load()
    segmented_words = wordsegment.segment(cleaned)
    return segmented_words


def detect_placement_and_count(input_string):
    pass