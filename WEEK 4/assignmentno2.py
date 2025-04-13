# Ask the user for a filename and handle errors
filename = input("Enter the name of the file to read: ")

try:
    # Open the input file in read mode
    with open(filename, 'r') as input_file:
        content = input_file.read()
    
    # Modify the content (example: replace "dfsdr" with "world")
    modified_content = content.replace("dfsdr", "world")
    
    # Write the modified content to a new file
    with open('modified_output.txt', 'w') as output_file:
        output_file.write(modified_content)
    
    print("File has been modified and saved as 'modified_output.txt'.")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except IOError:
    print(f"An error occurred while trying to read the file '{filename}'.")