import re
from collections import Counter
import json
# Common passwords and patterns
COMMON_PASSWORDS = {'password', '123456', 'qwerty', 'letmein', 'admin', 'abc123', 'welcome', 'monkey', 'password1', '12345678'}
COMMON_PATTERNS = ['123', 'abc', 'qwerty', '987', '098', '654', '543', '432', '321', 'zxcv', 'qaz', 'zaq', 'asdf']

# Character sets
UPPERCASE_LETTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
LOWERCASE_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
DIGITS = set('0123456789')
SPECIAL_CHARACTERS = set('!@#$%^&*()-_=+[{]}|;:,<.>/?"')

# Score weights for various aspects
LENGTH_WEIGHT = 4
COMMON_PASSWORD_WEIGHT = -8
COMMON_PATTERN_WEIGHT = -6
UPPERCASE_LETTER_WEIGHT = 2
LOWERCASE_LETTER_WEIGHT = 2
DIGIT_WEIGHT = 3
SPECIAL_CHARACTER_WEIGHT = 4

def count_character_groups(password):
    groups = []
    if any(char in UPPERCASE_LETTERS for char in password):
        groups.append('uppercase')
    if any(char in LOWERCASE_LETTERS for char in password):
        groups.append('lowercase')
    if any(char in DIGITS for char in password):
        groups.append('digits')
    if any(char in SPECIAL_CHARACTERS for char in password):
        groups.append('special_characters')
    return groups

def password_strength(password):
    score = 0

    # Length check
    length = len(password)
    score += length * LENGTH_WEIGHT

    # Common passwords check
    if password.lower() in COMMON_PASSWORDS:
        score += COMMON_PASSWORD_WEIGHT

    # Common patterns check
    for pattern in COMMON_PATTERNS:
        if pattern in password.lower():
            score += COMMON_PATTERN_WEIGHT

    # Character groups check
    groups = count_character_groups(password)
    score += len(groups) * (UPPERCASE_LETTER_WEIGHT + LOWERCASE_LETTER_WEIGHT +
                            DIGIT_WEIGHT + SPECIAL_CHARACTER_WEIGHT)

    # Count character frequency
    char_frequency = Counter(password)

    # Bonus for each unique character
    score += len(char_frequency)

    # Bonus for each repeated character
    score += sum(count - 1 for count in char_frequency.values() if count > 1)

    return score

def strength_rating(score):
    if score >= 60:
        return "Strong"
    elif score >= 30:
        return "Moderate"
    else:
        return "Weak"

def evaluate_feedback(score):
    if score >= 80:
        feedback = "Excellent! Your password is extremely strong and highly secure."
    elif score >= 60:
        feedback = "Great! Your password is strong and provides good security."
    elif score >= 40:
        feedback = "Good! Your password is moderate in strength, consider adding more complexity for better security."
    elif score >= 20:
        feedback = "Fair! Your password is weak, we recommend making it longer and adding a mix of characters."
    else:
        feedback = "Poor! Your password is very weak, please consider changing it immediately for better security."
    
    return feedback


def RunFullAnalysis(password):
    if password is None:
        return {}

    score = password_strength(password)
    strength = strength_rating(score)
    feedback = evaluate_feedback(score)

    response = {
        'Strength': strength,
        'Feedback': feedback
    }

    return json.dumps(response)