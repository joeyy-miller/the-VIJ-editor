# A simple command line text editor in Python

# Import the sys module for reading and writing files
import sys
import re

#Globals
VERSION = "1.0.1a"
BUILD = "03252023a"

# Check if a file name is given as an argument
if len(sys.argv) < 2:
    print("-------------------------- vij --------------------------")
    print("|  error: no input.                                     |")
    print("|  try:                                                 |")
    print("|  python3 vij.py [filename]                            |")
    print("---------------------------------------------------------")
    sys.exit(1)

# Open the file in read-write mode, or create a new file if it does not exist
filename = sys.argv[1]
try:
    file = open(filename, "r+")
except FileNotFoundError:
    file = open(filename, "w+")

# Read the file content into a list of lines
lines = file.readlines()

# Print the file content and the current line number
def print_file():
    print("-------------------------- vij --------------------------")
    print(f"Editing {filename}")
    for i, line in enumerate(lines):
        print(f"{i+1}: {line}", end="")

# Prompt the user for a command
def prompt():
    print("|-------------------- vij Commands ---------------------")
    print("|  a  - append a new line at the end                     |")
    print("|  i# - insert a new line before                         |")
    print("|  d#  - delete a given line number                      |")
    print("|  r#  - replace a given line number with a new line     |")
    print("|  s[q]  - save the file, q and quit                     |")
    print("|  h  - about the vij editor                             |")
    print("|  q  - quit without saving                              |")
    print("|  # - optional line number. [q] - optional paramter     |")
    print("--------------------------/ vij /-------------------------")
    return input("\nEnter a command: ")

# Loop until the user quits or saves
while True:
    # Print the file content and the current line number
    print_file()
    
    # Get the user command
    command = prompt()
    
    # Execute the command
    if command == "a":
        # Append a new line at the end
        new_line = input("Enter a new line: ")
        lines.append(new_line + "\n")
    
    elif command == "i":
        # Insert a new line before a given line number
        try:
            line_num = int(input("Enter a line number to insert before: "))
            if 1 <= line_num <= len(lines):
                new_line = input("Enter a new line: ")
                lines.insert(line_num - 1, new_line + "\n")
            else:
                print("Invalid line number.")
        except ValueError:
            print("Invalid line number.")
    elif re.match("i+[0-9][0-9]?", command):
        # Insert a new line before a given line number
        try:
            line_num = int(command[1:])
            if 1 <= line_num <= len(lines):
                new_line = input("Enter a new line: ")
                lines.insert(line_num - 1, new_line + "\n")
            else:
                print("Invalid line number.")
        except ValueError:
            print("Invalid line number.")
    elif command == "d":
        # Delete a given line number
        try:
            line_num = int(input("Enter a line number to delete: "))
            if 1 <= line_num <= len(lines):
                lines.pop(line_num - 1)
            else:
                print("Invalid line number.")
        except ValueError:
            print("Invalid line number.")
        
    elif re.match("d+[0-9][0-9]?", command):
        # Delete a given line
        try:
            # Strip off the letter of the command, leaving us with just the line # to delete.
            line_to_delete = int(command[1:])
            if 1 <= line_to_delete <= len(lines):
                lines.pop(line_to_delete - 1)
            else:
                print("Invalid line number.")
        except ValueError:
            print("Invalid line number.")
    
    elif command == "r":
        # Replace a given line number with a new line
        try:
            line_num = int(input("Enter a line number to replace: "))
            if 1 <= line_num <= len(lines):
                new_line = input("Enter a new line: ")
                lines[line_num - 1] = new_line + "\n"
            else:
                print("Invalid line number.")
        except ValueError:
            print("Invalid line number.")
    elif re.match("r+[0-9][0-9]?", command):
        try:
            line_num = int(command[1:])
            if 1 <= line_num <= len(lines):
                new_line = input("Enter a new line: ")
                lines[line_num - 1] = new_line + "\n"
            else:
                print("Invalid line number.")
        except ValueError:
            print("Invalid line number.")

    elif command == "h":
        # Output about the file editor
        print("                               ")
        print("+------  THE VIJ EDITOR ------+")
        print("|                             |")
        print("| (c) Joey Miller 2023        |")
        print("| version: " + VERSION + "             |")
        print("| build: " +  BUILD + "            |") 
        print("| lazy loading open source VI |")
        print("|                             |")   
        print("| made in sunny california    |")
        print("|                             |")
        print("+-----------------------------+")
        new_line = input("| Press any button to continue|")
    
    elif command == "s":
        # Save the file and exit
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        print(f"Saved {filename}.")

    elif command == "sq":
        # Save the file and exit
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        file.close()
        print(f"Saved {filename} and exited.")
        break

    elif command == "q":
        # Quit without saving
        file.close()
        print(f"Quit without saving {filename}.")
        break
    
    else:
        # Invalid command
        print("Invalid command.")
