import json
def find_repeated_character_combinations(s, min_string_length=4, min_integer_length=2, min_special_length=2):
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


print(find_repeated_character_combinations("Hello123!thisistesto123!"))