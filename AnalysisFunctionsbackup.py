import re
import wordsegment
#The standard way of structuring information to be passed to the front end is to place it into a dict and import the function into the app.py file 
#And call it inside the analyze_password(password) function. This call then be unpacked and combined with the final dict.
#Returns the amount of Sepcial Characters, Integers And Capital Letters
def search_special_int_caps(input_string):
    # Dict where the count of each occurence will be stored
    counts = {}
    # Iterate through each character in the string and search for the values specified.
    for char in input_string:
        if char.isalpha() and char.isupper():
            counts['Capital_Letter_amount'] = counts.get('Capital_Letter_amount', 0) + 1
        elif char.isdigit():
            counts['Integer_amount'] = counts.get('Integer_amount', 0) + 1
        elif not char.isalnum():
            counts['Special_Character_amount'] = counts.get('Special_Character_amount', 0) + 1
    # This checks the counts dict if any value was found. Basically makes sure that the function does not return anything unless somethign was found.
    result = {k: v for k, v in counts.items() if v > 0}
    #returns the resulting dict. will be empty if nothing is found.
    return result

def detect_words(input_string):

    cleaned = re.sub(r'[^a-zA-Z]', '', input_string) #remove any non letter characters
    wordsegment.load()
    segmented_words = wordsegment.segment(cleaned)
    results = {}
    results["Detected Words"] = segmented_words
    return results

def detect_first_and_last(input_string):
    results = {}
    if input_string[0].isupper() == True:
        results["First"] = "Capital"
    elif input_string[0].islower() == True:
        results["First"] = "Lower"
    elif input_string[0].isdigit() == True:
        results["First"] = "Integer"
    else:
        results["First"] = "Special"

    if input_string[-1].isupper() == True:
        results["Last"] = "Capital"
    elif input_string[-1].islower() == True:
        results["Last"] = "Lower"
    elif input_string[-1].isdigit() == True:
        results["Last"] = "Integer"
    else:
        results["Last"] = "Special"
    return results

def detect_integer_grouping(input_string):
    # Define a regular expression pattern to match integers
    integer_pattern = r'\d+'

    # Find all occurrences of integers in the input string
    integer_matches = re.finditer(integer_pattern, input_string)

    # Extract and return the indices of all integers
    indices = [(match.start(), match.end()) for match in integer_matches]
    if len (indices) > 1:
        return {"Integer_Grouping":False}
    elif len(indices) == 0:
        return {"Integer_Grouping":False}
    else:
        return {"Integer_Grouping":True}

def detect_integer_sequence(input_string):
    # Find all instances of integers in the input string
    integers_found = [int(x) for x in re.findall(r'\d+', input_string)]
    # Identify individual sequences
    results = {}
    for sequence in integers_found:
        count = 0
        sequence = str(sequence)
        for integer in sequence:
            integer = int(integer)
            count += 1
            try:
                if integer + 1 == int(sequence[count]):
                    pass
                elif integer - 1 == int(sequence[count]):
                    pass
                else:
                    
                    results[sequence] = False
                    break
                    
            except IndexError:
                results[sequence] = True
    return results

def detect_capital_letter_grouping(input_string):
    capital_indices = []
    for i, char in enumerate(input_string):
        if char.isupper():
            capital_indices.append(i)
    try:
        if capital_indices[0] + int(len(capital_indices)) >= capital_indices[-1]:
            return {"Capital_Letter_Grouping":True}
    except:
        return {"Capital_Letter_Grouping":False}

def detect_special_character_grouping(input_string):
    special_character_indices = []
    for i, char in enumerate(input_string):
        if char.isalpha() == False and char.isdigit() == False:
            special_character_indices.append(i)
    try:
        if special_character_indices[0] + int(len(special_character_indices)) > special_character_indices[-1]:
            return {"Special_Character_Grouping":True} 
    except IndexError:
        return {"Special_Character_Grouping":False}
    
def combine_and_jsonify(*dicts):
    try:
        
        for d in dicts:
            combined_dict.update(d)
        #return json.dumps(combined_dict, indent=4)
        return combined_dict
    except:
        combined_dict = {}
        for d in dicts:
            combined_dict.update(d)
        #return json.dumps(combined_dict, indent=4)
        return combined_dict

def RunFullAnalysis (string):
    if string == None:
        return
    spc_g = detect_special_character_grouping(string)
    cl_g = detect_capital_letter_grouping(string)
    i_s = detect_integer_sequence(string)
    i_g = detect_integer_grouping(string)
    f_l = detect_first_and_last(string)
    s_w = detect_words(string)
    ssic = search_special_int_caps(string)
    #This is intended to be json, but currently it is just one combined dict that is passed. 
    combined_dict = {}
    for d in [s_w, spc_g, ssic, cl_g, i_s, i_g, f_l]:
        combined_dict.update(d)
    return combined_dict

