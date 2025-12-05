try:
    with open("sample.txt","rt") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file \"sample.txt\" was not found.")