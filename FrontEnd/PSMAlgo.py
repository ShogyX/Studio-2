import re
import json

string = "ThisisatexT123!G"
s = "ThisisatexT123!G"
input_string = "ThisisatexT123!G"

#finds integer sequences and checks if they are at the end or beginning of a string and if they are the only occurence of integers in the string.
def find_integer_sequences(input_string, only_occurrence=True):
    # Find all instances of integers in the input string
    integers_found = [int(x) for x in re.findall(r'\d+', input_string)]
    
    # Identify individual sequences
    results = {}
    for sequence in integers_found:
        sequence_str = str(sequence)
        if len(sequence_str) > 1:  # Check if sequence is longer than 1 digit
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

    for char_type in ['uppercase', 'digit', 'special']:
        positions = []
        found_single_occurrence = False
        found_start = False
        found_end = False
        for i, char in enumerate(s):
            if char_type == 'uppercase' and char.isupper():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True

            elif char_type == 'digit' and char.isdigit():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True

            elif char_type == 'special' and not char.isalnum():
                positions.append(i)
                if len(positions) > 1:
                    found_single_occurrence = False
                else:
                    found_single_occurrence = True
                if i == 0:
                    found_start = True
                elif i == len(s) - 1:
                    found_end = True

        results[char_type] = {
            'single_occurrence': found_single_occurrence,
            'start': found_start,
            'end': found_end
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
                'valid': True,
                'start_occurrence': start_occurrence,
                'end_occurrence': end_occurrence,
                'only_occurrence': only_occurrence_flag
            }

        i = j

    return json.dumps(results, indent=4)

#Finds repeated character combinations that are equal to or longer than 4 in length for integers, letters and special characters.
def find_repeated_combinations(s, min_string_length=4, min_integer_length=4, min_special_length=4):
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
    results = []
    for match, is_start, is_end, match_type in filtered_matches:
        results.append({
            "combination": match,
            "type": match_type,
            "times_repeated": s.count(match)
        })
    
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

