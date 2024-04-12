import json
import csv
import re

def contains_integers_or_special_chars(s):
    # Regular expression to match integers or special characters
    regex = re.compile(r'[0-9!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>/?]')
    return bool(regex.search(s))

def convert_from_leet(input_string):
    leetspeak_dict = {
    'a': ['4', '@', 'A', 'a', '/\\', '/-\\'],
    'b': ['8', 'B', '|3', 'b', '13', '!3', '6', 'I3', '!3', '/3'],
    'c': ['(', '[', '{', '<', 'C', 'c'],
    'd': ['|)', '|]', 'D', 'd', 'cl', 'cI', 'I)', 'I]'],
    'e': ['3', 'E', 'e', '[-'],
    'f': ['|=', 'F', 'f', '/=', 'I=', 'ph'],
    'g': ['6', '9', 'G', 'g', '(_-', '(_+', 'C-', '[,'],
    'h': ['#', '|-|', 'H', 'h', '|~|', 'I-I', 'I~I', ']-[', ']~[', '}{', ')-(', '(-)', ')~(', '(~)'],
    'i': ['1', '!', '|', 'I', 'i', '[]'],
    'j': ['_|', 'J', 'j'],
    'k': ['|<', 'K', 'k', '|c', 'Ic', '|{', '|('],
    'l': ['1', '|_', 'L', 'l', '|', '7'],
    'm': ['|\\/|', 'M', 'm'],
    'n': ['|\\|', 'N', 'n'],
    'o': ['0', 'O', 'o', '<>'],
    'p': ['|D', '|o', 'P', 'p'],
    'q': ['(,)', 'Q', 'q'],
    'r': ['|2', 'R', 'r'],
    's': ['5', '$', 'S', 's'],
    't': ['7', '+', 'T', 't', '-|-', '~|~'],
    'u': ['|_|', 'U', 'u', '(_)', 'L|'],
    'v': ['\\/', 'V', 'v'],
    'w': ['\\/\\/', 'VV', '\\N', '\'//', '\\\'', '\\^/', '(n)', '\\V/', '\\X/', '\\|/', '\\_|_/', '\\_:_/', 'uu', '2u', '\\\\//\\\\//', 'w', 'W'],
    'x': ['%', '><', 'X', 'x'],
    'y': ['`/', '7', '\\|/', '\\//', 'Y', 'y'],
    'z': ['2', '7_', '-/_', '%', '>', '~/_', '-\\_', '-|_', 'z', 'Z'],
    ' ': ['-', '_', ' '],
    }
    new_word = input_string
    new_words = []
    for letter in leetspeak_dict.keys():
        list_of_subs = leetspeak_dict[letter]
        for sub in list_of_subs:
            if sub in input_string:
                new_word = new_word.replace(sub, letter)
                if new_word not in new_words:
                    new_words.append(new_word)
    
    return new_word

def search_file(search_term, filename='FrontEnd/all_words.txt'):

    if contains_integers_or_special_chars(search_term) == True:
        search_term_2 = convert_from_leet(search_term)
    else:
        search_term_2 = ""

    rows = []
    search_term = search_term.lower()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[1].lower() in search_term:
                rows.append(row)
                #print(row)
            elif row[1].lower() in search_term_2:
                row[2] = "Leet Match"
                rows.append(row)


    output = rows
    output_lower = [[lang, word.lower(), source] for lang, word, source in output]
    output_lower.sort(key=lambda x: len(x[1]), reverse=True)
    filtered_output = []
    added_words = set()
    for item in output_lower:
        word = item[1]
        is_substring = False
        for other_word in added_words:
            if word in other_word:
                is_substring = True
                break
        if not is_substring:
            filtered_output.append(item)
            added_words.add(word)

    # Convert filtered output to JSON format
    json_output = []
    for item in filtered_output:
        json_output.append({
            "language": item[0],
            "word": item[1],
            "source": item[2]
        })

    # Convert the list of dictionaries to JSON
    return json.dumps(json_output, indent=4)

input_string = "pasword"

database_results = json.loads(search_file(input_string))
for dict in database_results:
    language = dict["language"]
    word_found = dict["word"]
    word_source = dict["source"]
