try:
    with open("output.txt","wt") as file:
        script = input("Enter text to write to the file: ")
        file.write(f"{script}\n")
except FileNotFoundError:
    print("Error: The file \"output.txt\" was not found.")
else:
    print("Data successfully written to output.txt.\n")

try:
    with open("output.txt","a+") as file1:
        add_script = input("Enter additional text to append: ")
        file1.write(add_script)
        file1.seek(0)
        content = file1.read()
except FileNotFoundError:
    print("Error: The file \"output.txt\" was not found.")
else:
    print("Data successfully appended.\n")
    print("Final content of output.txt:")
    print(content)



