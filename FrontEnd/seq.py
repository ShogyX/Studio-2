import json

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