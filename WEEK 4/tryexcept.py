try:
    with open("examples.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
        print("File not found. Please check the filename.")
 