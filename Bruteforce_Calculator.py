import string

#Currently work in progress. Provides false calculations when multiple characters types are used.

def generate_charset(password):
    return ''.join([
        string.ascii_lowercase if any(char.islower() for char in password) else '',
        string.ascii_uppercase if any(char.isupper() for char in password) else '',
        string.digits if any(char.isdigit() for char in password) else '',
        string.punctuation if any(char in set(string.punctuation) for char in password) else ''
    ])

def time_to_crack_password(password, attempts_per_second):
    password_length = len(password)
    charset = generate_charset(password)
    total_combinations = len(charset) ** password_length
    time_seconds = total_combinations / attempts_per_second
    return time_seconds, time_seconds / 60, time_seconds / 3600, time_seconds / 86400, time_seconds / (86400 * 30), time_seconds / (86400 * 365)

input_password = input("Enter the password: ")
attempts_per_second = 2071500000  # Example: 2.07 Billion attempts per second (depends on computational power)

time_seconds, time_minutes, time_hours, time_days, time_months, time_years = time_to_crack_password(input_password, attempts_per_second)

print("Time to crack password:")
print("Seconds:", time_seconds)
print("Minutes:", time_minutes)
print("Hours:", time_hours)
print("Days:", time_days)
print("Months:", time_months)
print("Years:", time_years)