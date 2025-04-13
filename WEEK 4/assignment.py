# Read from the input file and write to a new file with modifications
try:
    # Open the input file in read mode
    with open('output.txt', 'r') as input_file:
        content = input_file.read()
    
    # Modify the content (example: replace "dfsdr" with "world")
    modified_content = content.replace("dfsdr", "world")
    
    # Write the modified content to a new file
    with open('modified_output.txt', 'w') as output_file:
        output_file.write(modified_content)
    
    print("File has been modified and saved as 'modified_output.txt'.")
except FileNotFoundError:
    print("The input file does not exist.")