import re
import json
import csv


def search_db_alpha(input_string, disable_leet=True):
    
    def contains_integers_or_special_chars(input_string):
        # Regular expression to match integers or special characters
        regex = re.compile(r'[0-9!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>/?]')
        return bool(regex.search(input_string))

    def convert_from_leet(input_string):
        leetspeak_dict = {
        'a': ['4', '@', 'A', 'a'],
        'b': ['8', 'B', '|3', 'b', '13'],
        'c': ['(', '[', '{', '<', 'C', 'c'],
        'd': ['|)', '|]', 'D', 'd'],
        'e': ['3', 'E', 'e', ],
        'f': ['|=', 'F', 'f', 'ph'],
        'g': ['6', '9', 'G', 'g'],
        'h': ['#', '|-|', 'H', 'h'],
        'i': ['1', '!', 'I', 'i'],
        'j': ['_|', 'J', 'j'],
        'k': ['|<', 'K', 'k'],
        'l': ['1', '|_', 'L', 'l', '|', '7'],
        'm': ['M', 'm'],
        'n': ['N', 'n'],
        'o': ['0', 'O', 'o', '<>'],
        'p': ['|D', '|o', 'P', 'p'],
        'q': ['Q', 'q'],
        'r': ['|2', 'R', 'r'],
        's': ['5', '$', 'S', 's'],
        't': ['7', '+', 'T', 't'],
        'u': ['|_|', 'U', 'u',],
        'v': ['\\/', 'V', 'v'],
        'w': ['VV', '2u''w', 'W'],
        'x': ['%', '><', 'X', 'x'],
        'y': ['`/', '7', '\\|/', '\\//', 'Y', 'y'],
        'z': ['2', '7_', '>', 'z', 'Z'],
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

    def search_file(input_string):

        
        if contains_integers_or_special_chars(input_string) == True and disable_leet == False:
            input_string_2 = convert_from_leet(input_string)
        else:
            input_string_2 = ""

        rows = []
        input_string = input_string.lower()

        
        length_input = len(input_string)
        if length_input > 33:
            length_input = 33


        remaining_length = length_input
        

        while remaining_length > 3:
            changes_made = 0
            filename = "output/output_files/wordlist"
            filename = filename + f"_{remaining_length}.txt"

            with open(filename, 'r', encoding='utf-8') as f:
                
                for row in f:
                    row = row.strip()
                    if row.lower() in input_string and row not in rows or row.lower() in input_string_2:
                        rows.append(row)
                        remaining_length -= len(row)
                        if len(row) > remaining_length/2:
                            break
                        changes_made += 1
                        
                    # elif row.lower() in input_string_2 and row not in rows:
                    #     rows.append(row)
                    #     remaining_length -= len(row)
                    #     if len(row) > remaining_length/2:
                    #         break
                    #     changes_made += 1
                
            if changes_made == 0:
                remaining_length = 0

        output_lower = rows
        
        #output_lower = [[lang, word.lower(), source] for lang, word, source in output]
        output_lower.sort(key=lambda x: len(x), reverse=True)
        filtered_output = []
        added_words = set()
        for item in output_lower:
            word = item
            is_substring = False
            for other_word in added_words:
                if word.lower() in other_word.lower():
                    is_substring = True
                    break
            if not is_substring:
                filtered_output.append(item)
                added_words.add(word)

        # Convert filtered output to JSON format
        json_output = []
        for item in filtered_output:
            json_output.append({
                "word": item
            })

        # Convert the list of dictionaries to JSON
        
        return json.dumps(json_output, indent=4)

    #search_file(input_string)
    return search_file(input_string)

#The following function will search the password of the user against a wordlist of 11 million common words using a leet converter and the raw input.
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

#this will search for combinations of letters in alphabetical order longer than 2
def search_abcs(input_string):
    org_string = input_string
    matching_string = "abcdefghijklmnopqrstuvwxyzæøå"
    matches = []
    match_length = 1
    current_match = ""
    for i, letter in enumerate (input_string.lower()):
        if letter.isalpha() == True:
            try:
                index_in_alphabet = matching_string.index(letter)
                if input_string.lower()[i+1] == matching_string[index_in_alphabet+1]:
                    current_match += org_string[i]
                    match_length += 1

                elif match_length > 2:
                    current_match += org_string[i]
                    matches.append(current_match)
                    match_length = 1
                    current_match = ""

                else:
                    match_length = 1
                    current_match = ""

            except IndexError as e:
                if match_length > 2:
                    current_match += org_string[i]
                    matches.append(current_match)
                    match_length = 1
                    current_match = ""   


    return matches

#finds integer sequences and checks if they are at the end or beginning of a string and if they are the only occurence of integers in the string.
def find_integer_sequences(input_string, only_occurrence=True):
    # Find all instances of integers in the input string
    integers_found = [int(x) for x in re.findall(r'\d+', input_string)]
    
    # Identify individual sequences
    results = {}
    for sequence in integers_found:
        sequence_str = str(sequence)
        if len(sequence_str) > 2:  # Check if sequence is longer than 1 digit
            count = 0
            for i in range(len(sequence_str) - 1):
                if abs(int(sequence_str[i]) - int(sequence_str[i + 1])) == 1:
                    count += 1
                else:
                    break
            else:  # If loop completes without breaking, it's a valid sequence
                start_occurrence = input_string.startswith(sequence_str)
                end_occurrence = input_string.endswith(sequence_str)
                if only_occurrence and len(integers_found) == 1:
                    only_occurrence_flag = True
                else:
                    only_occurrence_flag = False
                results[sequence_str] = {
                    'start_occurrence': start_occurrence,
                    'end_occurrence': end_occurrence,
                    'only_occurrence': only_occurrence_flag
                }

    return json.dumps(results, indent=4)

#finds integers, uppercase and special characters, and checks if they are at the end or beginning of a string and if they are the only occurence in the string.
def find_character_positions(s):
    results = {}

    for char_type in ['uppercase letter', 'number', 'special-character', 'lowercase letter']:
        positions = []
        found_single_occurrence = False
        found_start = False
        found_end = False
        found_middle = False
        
        for i, char in enumerate(s):
            if char_type == 'lowercase letter' and char.islower():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True
                else:
                    found_middle = True  # Set found_middle to True if character is in the middle
                    
            elif char_type == 'uppercase letter' and char.isupper():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True
                else:
                    found_middle = True  # Set found_middle to True if character is in the middle

            elif char_type == 'number' and char.isdigit():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True
                else:
                    found_middle = True  # Set found_middle to True if character is in the middle

            elif char_type == 'special-character' and not char.isalnum():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True
                else:
                    found_middle = True  # Set found_middle to True if character is in the middle

        results[char_type] = {
            'single_occurrence': found_single_occurrence,
            'start': found_start,
            'end': found_end,
            'middle': found_middle 
        }

    return json.dumps(results, indent=4)

#finds character sequences longer than 2 in length, is case sensitive.
def find_character_sequences(input_string, sequence_length=3, only_occurrence=True):
    # Identify individual sequences
    results = {}
    i = 0
    while i < len(input_string):
        sequence = input_string[i]
        j = i + 1
        while j < len(input_string) and input_string[j] == input_string[i]:
            sequence += input_string[j]
            j += 1

        if len(sequence) >= sequence_length:
            start_occurrence = i == 0
            end_occurrence = j == len(input_string)
            if only_occurrence and input_string.count(sequence) == 1:
                only_occurrence_flag = True
            else:
                only_occurrence_flag = False
            results[sequence] = {
                #'start_occurrence': start_occurrence,
                #'end_occurrence': end_occurrence,
                'only_occurrence': only_occurrence_flag
            }

        i = j

    return json.dumps(results, indent=4)

#Finds repeated character combinations that are equal to or longer than 4 in length for integers, letters and special characters.
def find_repeated_character_combinations(s, min_string_length=4, min_integer_length=4, min_special_length=4):
    matches = []
    
    # Find repeated string combinations
    for i in range(len(s) - min_string_length + 1):
        for j in range(i + min_string_length, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= min_string_length and s.count(substring) > 1:
                matches.append((substring, i == 0, j == len(s), "string"))
    
    # Find repeated integer combinations
    for i in range(len(s) - min_integer_length + 1):
        for j in range(i + min_integer_length, len(s) + 1):
            substring = s[i:j]
            if substring.isdigit() and len(substring) >= min_integer_length and s.count(substring) > 1:
                matches.append((substring, i == 0, j == len(s), "integer"))
    
    # Find repeated special character combinations
    for i in range(len(s) - min_special_length + 1):
        for j in range(i + min_special_length, len(s) + 1):
            substring = s[i:j]
            if not substring.isalnum() and len(substring) >= min_special_length and s.count(substring) > 1:
                matches.append((substring, i == 0, j == len(s), "special character"))
    
    # Sort matches by length, longest first
    matches.sort(key=lambda x: len(x[0]), reverse=True)
    
    # Filter out shorter matches that are subsumed by longer ones
    filtered_matches = []
    for match, is_start, is_end, match_type in matches:
        if not any(match in longer_match for longer_match, _, _, _ in filtered_matches):
            filtered_matches.append((match, is_start, is_end, match_type))
    
    # Prepare results in JSON format
    results = {}
    for match, is_start, is_end, match_type in filtered_matches:
        results[match] = {
            "type": match_type,
            "times_repeated": s.count(match)
        }
    
    return json.dumps(results, indent=4)

#Checks for the inclusion of the different character types.
def check_character_types(s):
    has_lowercase_alpha = any(c.islower() for c in s)
    has_uppercase_alpha = any(c.isupper() for c in s)
    has_numeric = any(c.isdigit() for c in s)
    has_special = any(not c.isalnum() for c in s)

    result = {
        "lowercase": has_lowercase_alpha,
        "uppercase": has_uppercase_alpha,
        "integer": has_numeric,
        "special": has_special
    }

    return json.dumps(result, indent=4)


def retrieve_password_fallacy(fallacy_name, json_file_path="FrontEnd/responses.json"):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    return data.get(fallacy_name)


def umbrellafunc (input_string):

    issues_found = 0
    password_info = {"Length Requirement!":[], "Common Sequence of Numbers!":[], "Repeated Letter Sequence!":[], "Predictable Character Placement!":[], "Repeated Combinations!":[], "Missing Character Type!":[], "Predictable Character Sequence!":[], "Match in Database!":[]}
    #check the length
    if len(input_string) < 12:
        Rule_Type = "Length Requirement!"
        issues_found += 1
        password_info[Rule_Type].append("Your Password is too short! We recommend more than 12 characters in length!")
        #Length is short


    # elif len(input_string) > 8 and len(input_string) < 12:
    #     #Length is moderate
    #     Rule_Type = "Length Requirement!"
    #     issues_found += 1
    #     password_info[Rule_Type].append("Your Password is above the minimum requirement, but would benefit from being above 12 characters long!")
        

    #find abcs

    abcs_found = search_abcs(input_string)
    for combination in abcs_found:
        Rule_Type = "Predictable Character Sequence!"
        if len(combination) > 2:
            issues_found += 1
            password_info[Rule_Type].append(f"The following alphabetical sequence {combination} was found in your password!")

    # Find integer sequences
    integer_sequences_json = find_integer_sequences(input_string)
    integer_sequences_data = json.loads(integer_sequences_json)
    integer_sequences_found = []
    character_repetitions_found = []

    for key, value in integer_sequences_data.items():
        Rule_Type = "Common Sequence of Numbers!"
        #This is the integer sequence that was found
        if len(key) > 1:
            integer_sequences_found.append(key)
        #check specs
        at_start = value["start_occurrence"]
        at_end = value["end_occurrence"]
        only_instance = value["only_occurrence"]

        if only_instance == True and at_end == True:
            password_info[Rule_Type].append("All the numbers in your password are in an easy to guess sequence and placed at the end of the password which is easy to guess")
            issues_found += 1
            # all integers in password are at the end in a sequence

        elif only_instance == True and at_start == True:
            password_info[Rule_Type].append("All the numbers in your password are in an easy to guess sequence and placed at the beginning of the password which is easy to guess")
            issues_found += 1
            # all integers in password are at the start in a sequence

        elif only_instance == True:
            password_info[Rule_Type].append("All the numbers in your password are in an easy to guess sequence")
            issues_found += 1
            # all integers in password are grouped in a sequence 
        
        elif at_end == True and at_start == True:
            password_info[Rule_Type].append("You have repeated an easy to guess number sequence at the end and beginning of your password!")
            issues_found += 1
            # repeated combo at the start and beginning

        elif only_instance == False:
            password_info[Rule_Type].append("You have included an easy to guess number sequence in your password!")
            issues_found += 1
            # found sequential combination of integers in password

    # Find grouped character repetitions
    find_character_sequences_json = find_character_sequences(input_string)
    find_character_sequences_data = json.loads(find_character_sequences_json)

    
    for key, value in find_character_sequences_data.items():
        Rule_Type = "Repeated Letter Sequence!"
        if len(key) > 2:
            only_instance = value["only_occurrence"]
        character_repetitions_found.append(key)

        if only_instance == True:
            password_info[Rule_Type].append("You have included a sequence of repeated letters in your password!")
            issues_found += 1
        else:
            #Multiple instances of repeated characters.
            issues_found += 1
            password_info[Rule_Type].append("You have included multiple sequences of repeated letters in your password!")

    # Find issues in character placement and occurences
    find_character_positions_json = find_character_positions(input_string)
    find_character_positions_data = json.loads(find_character_positions_json)


    for key, value in find_character_positions_data.items():
        Rule_Type = "Predictable Character Placement!"
        at_start = value["start"]
        at_end = value["end"]
        at_middle = value["middle"]
        only_instance = value["single_occurrence"]

        if at_middle == False:
            if at_end == True and at_start == False:
                issues_found += 1
                #single instance at the end
                password_info[Rule_Type].append(f"The only instance of a {key} in your password is at the beginning of the password")
                
            elif at_end == False and at_start == True:
                issues_found += 1
                #single instance at the start
                password_info[Rule_Type].append(f"The only instance of a {key} in your password is at the start of the password")
                
            elif at_start == True and at_end == True:
                if input_string[0] == input_string[-1]:
                    issues_found += 1
                    #both instances of the character are at the beginning and end, and match.
                    password_info[Rule_Type].append(f"The only two instances of a {key} in your password is at the end and end of the password")

    # Find issues in repeated combinations of letters, digits and or special characters.
    find_repeated_character_combinations_data = json.loads(find_repeated_character_combinations(input_string))
    statements = []
    for key, value in find_repeated_character_combinations_data.items():
        Rule_Type = "Repeated Combinations!"
        combination = key
        type = value["type"]
        times_repeated = value["times_repeated"]
        if times_repeated > 1:
            issues_found += 1
            #Configure a statement to take in the combination and the times it was repeated. like
            password_info[Rule_Type].append(f"The following combination '{combination}' was repeated within your password {times_repeated} times!")
            

    
    # Check if password contains all character types!
    check_character_types_data = json.loads(check_character_types(input_string))
    for key, value in check_character_types_data.items():
        Rule_Type = "Missing Character Type!"
        if value == False:
            if key == "lowercase":
                #Add lacks lowercase character statement
                password_info[Rule_Type].append("Your password lacks the inclusion of a lowercase letter")
                issues_found += 1
            elif key == "uppercase":
                issues_found += 1
                #Add lacks lowercase character statement
                password_info[Rule_Type].append("Your password lacks the inclusion of a uppercase letter")

            elif key == "integer":
                issues_found += 1
                #Add lacks lowercase character statement
                password_info[Rule_Type].append("Your password lacks the inclusion of a number")

            elif key == "special":
                issues_found += 1
                #Add lacks lowercase character statement
                password_info[Rule_Type].append("Your password lacks the inclusion of a special character")

    database_results = json.loads(search_db_alpha(input_string))
    if len(database_results) > 0:
        words_found = []

        
        for word in database_results:
            
            #language = dict["language"]
            #word_found = dict["word"]
            #word_source = dict["source"]
            words_found.append(word["word"])
            issues_found += 1
            #password_info['Match in Database!'].append(f"{word_found}")

        if len(words_found) <= 1:
            password_info['Match in Database!'].append(f"Your password contains a word that is in our database: {words_found}")
        else:
            password_info['Match in Database!'].append(f"Your password contains multiple words that are in our database: {words_found}")

    password_info["Issues Found"] = issues_found
    return json.dumps(password_info)
