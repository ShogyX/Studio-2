import re

def find_years(string):
    pattern = re.compile(r'\b\d{4}\b|\D(\d{4})\D')
    matches = pattern.findall(string)
    years = []
    for match in matches:
        if match.isdigit():
            years.append(match)
        else:
            # Extract only the digits from the matched pattern
            year = re.search(r'\d{4}', match)
            if year:
                years.append(year.group())
    return years
