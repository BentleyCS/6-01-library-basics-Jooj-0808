#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    try:
        with open(fileName, 'r') as file:
            longest_line = max(file, key=len, default="")
        return longest_line
    except FileNotFoundError:
        print(f"Error: The file '{fileName}' was not found.")
        return ""

def toBinary(fileName):
    return [fileName[i:i+8] for i in range(0, len(fileName), 8)]
