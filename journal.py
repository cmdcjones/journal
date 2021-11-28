# Project to understand File Handling in Python

# TODO: 
# understand file opening modes
# create, read, and update files
# use while loop with input as menu

# -------------------------------------------------------------
import sys

def write_entry():
    journal = open("journal.txt", "a")
    entry = input("Write your entry below:\n\n")
    journal.write(entry)
    print("Saving your entry...")
    journal.close()
    print("Saved!")

def read_journal():
    journal = open("journal.txt")
    print(journal.read())

def main():
    print("Welcome to the journal!")
    while True:
        action = int(input("""1 - Write new entry
2 - Read the journal
3 - Exit
"""))
        if action == 1:
            write_entry()
        if action == 2:
            read_journal()
        if action == 3:
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
# -------------------------------------------------------------

# the open() function is the key function for working with files
# 'r' - Read; Default value. Opens a file for reading
# 'a' - Append. Opens a file for appending, creates file if it does not exist
# 'w' - Write. Opens a file for writing, creates file if it does not exist
# 'x' - Create. Creates the specified file, returns error if file does not exist

# file_ = open("demonstration.txt")
# print(file_.read())
# file_.close()

# if the file is located in a different location, you will have to specify the file path
# file_ = open("C:\Users\Dom\Documents\Coding\Python\Projects\journal\demonstration.txt")

# by default read() returns the whole text, but a specific number of characters can be specified
# print(file_.read(5))

# readline() can be used to return one line
# print(file_.readline())

# it is good practice to close the file when you are done with it
# closing the file will also allow it to be updated if the file needs to be read again
# file_.close()

# 'a' will append to the end of the file
# 'w' will overwrite any existing content

# file_ = open("demonstration.txt", 'a')
# file_.write("\nThis file has been updated 11/26 11:43PM.")
# file_.close()
# file_ = open("demonstration.txt")
# print(file_.read())
# file_.close()

# to delete a file, import the os module and run the remove() function