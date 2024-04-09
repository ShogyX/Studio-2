import re

string = "ThisisatexT123!G"
input_string = "ThisisatexT123!G"

def measure_string_length(string):
    length = len(string)
    first_index = 0 if length == 0 else 0
    last_index = length - 1 if length > 0 else None
    return length, first_index, last_index

# Example usage:
length, first_index, last_index = measure_string_length(input_string)
print("String Length:", length)
print("First Index Position:", first_index)
print("Last Index Position:", last_index)


def find_integer_sequences(input_string):
    # Find all instances of integers in the input string
    integers_found = [int(x) for x in re.findall(r'\d+', input_string)]
    
    # Identify individual sequences
    results = {}
    for sequence in integers_found:
        count = 0
        sequence = str(sequence)
        start_index = input_string.find(sequence)
        end_index = start_index + len(sequence) -1
        for integer in sequence:
            integer = int(integer)
            count += 1
            try:
                if integer + 1 == int(sequence[count]):
                    pass
                elif integer - 1 == int(sequence[count]):
                    pass
                else:
                    results[sequence] = {'valid': False, 'start_index': start_index, 'end_index': end_index}
                    break
            except IndexError:
                results[sequence] = {'valid': True, 'start_index': start_index, 'end_index': end_index}
    return results

# Example usage:
sequences_found = find_integer_sequences(input_string)
print("Integer sequences found:", sequences_found)


def find_character_positions(s):
    uppercase_positions = []
    digit_positions = []
    special_positions = []

    for i, char in enumerate(s):
        if char.isupper():
            uppercase_positions.append(i)
        elif char.isdigit():
            digit_positions.append(i)
        elif not char.isalnum():
            special_positions.append(i)

    return {
        'uppercase_positions': uppercase_positions,
        'digit_positions': digit_positions,
        'special_positions': special_positions
    }

# Example usage:
positions = find_character_positions(string)
print("Uppercase positions:", positions['uppercase_positions'])
print("Digit positions:", positions['digit_positions'])
print("Special character positions:", positions['special_positions'])


def find_words_with_indices(string, word_database):
    found_words = []
    for word in word_database:
        start_index = string.find(word)
        if start_index != -1:
            end_index = start_index + len(word) - 1
            found_words.append({'word': word, 'start_index': start_index, 'end_index': end_index})
    return found_words

# Example usage:
word_database = ["sample", "words", "some", "not", "in", "database"]
found_words = find_words_with_indices(string, word_database)
print("Words found in the string:")
for word_info in found_words:
    print("Word:", word_info['word'])
    print("Start Index:", word_info['start_index'])
    print("End Index:", word_info['end_index'])
