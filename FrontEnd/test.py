from faker import Faker

fake = Faker()

def generate_word_list(num_words):
    word_list = [fake.word() for _ in range(num_words)]
    return word_list

# Generate a list of 1 million words
million_words = generate_word_list(1000000)

# Print the first 10 words as an example
print("Created List")



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie(word_database):
    root = TrieNode()
    for word in word_database:
        current = root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    return root

def search_words_with_indices(string, root):
    def search_from_index(index, node):
        current = node
        word_start = index
        while index < len(string) and string[index] in current.children:
            current = current.children[string[index]]
            index += 1
            if current.is_end_of_word:
                found_words.append({'word': string[word_start:index], 'start_index': word_start, 'end_index': index - 1})

    found_words = []
    for i in range(len(string)):
        search_from_index(i, root)
    return found_words

# Example usage:
string = "This is a sample string containing some words."
word_database = million_words

# Build Trie from word database
trie_root = build_trie(word_database)
print("built trie root")

# Search for words in the string using the Trie
found_words = search_words_with_indices(string, trie_root)
print("Words found in the string:")
for word_info in found_words:
    print("Word:", word_info['word'])
    print("Start Index:", word_info['start_index'])
    print("End Index:", word_info['end_index'])



#This builds the trie from an sql query:

import sqlite3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie_from_query_results(cursor):
    root = TrieNode()
    for row in cursor.fetchall():
        word = row[0]  # Assuming the word is in the first column
        current = root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    return root

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Execute the SQL query
cursor.execute("SELECT word FROM words")

# Build the Trie from the query results
trie_root = build_trie_from_query_results(cursor)

# Close the database connection
conn.close()
