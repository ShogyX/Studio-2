import os  # Import the os module for file handling
import re  # Import the re module for regular expressions

def sanitize_passwords(input_file):
    """
    Sanitize the passwords in the input file by escaping special characters.
    :param input_file: The path to the input file containing the passwords.
    :return: A list of escaped passwords.
    """
    with open(input_file, 'r') as file:  # Open the input file in read mode.
        passwords = file.readlines()  # Read the passwords from the input file.

    escaped_passwords = [re.escape(password.strip()) for password in passwords]  # Escape the special characters in each password.
    return escaped_passwords

def write_to_file(escaped_passwords, output_file):
    """
    Write the escaped passwords to the output file.
    :param escaped_passwords: The list of escaped passwords to write.
    :param output_file: The path to the output file.
    """
    with open(output_file, 'w') as file:  # Open the output file in write mode.
        for password in escaped_passwords:
            file.write(f"{password}\n")  # Write each escaped password to the output file.

if __name__ == "__main__":  # Entry point of the script.
    if len(sys.argv) != 2:  # Check if the input file is provided as an argument.
        print("Usage: python sanitize_passwords.py <input_file.txt>")
        sys.exit(1)

    input_file = sys.argv[1]  # Get the path to the input file from the first argument.

    if not os.path.isfile(input_file):  # Check if the input file exists.
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    escaped_passwords = sanitize_passwords(input_file)  # Sanitize the passwords.
    write_to_file(escaped_passwords, 'sanitized_pwd_list.txt')  # Write the sanitized passwords to the output file.
    print("Successfully sanitized the passwords and saved to sanitized_pwd_list.txt")  # Confirmation message.