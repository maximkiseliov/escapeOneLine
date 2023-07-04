import json
import pyperclip

# Receive JSON as input string
input_string = input("Enter JSON input: ")

# Escape required characters
escaped_string = json.dumps(input_string)

# Use double quotes instead of single quotes
double_quoted_string = escaped_string.replace("'", '"')

# Make it in one line
one_line_string = double_quoted_string.replace('\n', '')

# Copy to clipboard
pyperclip.copy(one_line_string)

# Print to user
print("Escaped JSON (copied to clipboard):", one_line_string)

# Ask user for new input
new_input_string = input("Enter new JSON input: ")
