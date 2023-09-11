#This is a code I made for a one time  use with the help of chatGPT3.5 
#It places a } at the end of each sentence and writes the next sentence in the new line 
#If you sentence ends with a ","or "." make sure to change it in line 21 where \s stands for space 

import re

# Function to add a closing curly brace to each sentence
def add_closing_brace(sentence):
    return sentence.strip() + "}"

# Read the input file
input_file = 'input.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your desired output file name

with open(input_file, 'r') as file:
    content = file.read()

# Use a regular expression to split the content into sentences
# You can customize the regex pattern based on your specific sentence structure
# This example assumes that sentences end with a period followed by a space.
sentences = re.split('\s', content)

# Add a closing curly brace to each sentence
sentences_with_brace = [add_closing_brace(sentence) for sentence in sentences]

# Join the sentences back together
modified_content = chr(10).join(sentences_with_brace)

# Write the modified content to the output file
with open(output_file, 'w') as file:
    file.write(modified_content)

print(f"Closing curly braces added and saved to {output_file}")

