import re
#The standard way of structuring information to be passed to the front end is to place it into a dict and import the function into the app.py file 
#And call it inside the analyze_password(password) function. This call then be unpacked and combined with the final dict.

def search_special_int_caps(text):
    #More logic is needed so that the function only returns something if it finds anything. else it shoudl return nothing.
    results = {
        "special_characters": 0,
        "integers": 0,
        "capitalized_letters": 0
    }
    
    special_characters = re.findall(r'[^a-zA-Z0-9\s]', text)
    integers = re.findall(r'\d', text)
    capitalized_letters = re.findall(r'[A-Z]', text)
    
    if special_characters:
        #This adds the character to the dict
        results["special_characters"] = special_characters
    if integers:
        #This adds the integer to the dict
        results["integers"] = integers
    if capitalized_letters:
        #This adds the letter to the dict
        results["capitalized_letters"] = capitalized_letters
    
    return results
