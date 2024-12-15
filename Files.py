'''
Objective: Write a program to count and print the number of lines in a given text file.

Example:

Input File ("example.txt"):

Line 1
Line 2
Line 3

Output: 3
'''

def fileLines():
    file = open(input("Enter your file: "), "r")

    length = len(file.readlines())

    file.close()

    print(length)


'''
Objective: Read a file and extract all words from the first line of the text and write them into a new file, one word per line.

Example:
Input File ("input.txt"):

Hello world from Python
Another line here

Output File ("words.txt"):

Hello
world
from
Python
'''

def wordCollector():
    file = open(input("Enter your file: "), "r")

    firstLine = file.readline()

    firstLine = firstLine.split(" ")

    new = open("words.txt", "w")

    for i in firstLine:
        new.write(i + "\n")

    file.close()
    new.close()


'''
Task 3: Concatenate Files

Objective: Given two text files, read them and create a new text file that contains the content of both, with the second file's content appended to the first file's content.

Example:

Input File 1 ("file1.txt"):

Hello from file 1

Input File 2 ("file2.txt"):

Hello from file 2

Output File ("output.txt"):

Hello from file 1
Hello from file 2
'''

def concatenateFiles():
    file1 = open("text.txt", "r") #open(input("Enter your file: "), "r")
    file2 = open("words.txt", "r") #open(input("Enter your file: "), "r")

    file1 = " ".join(file1.readlines())
    file2 = " ".join(file2.readlines())

    new = open("cf.txt", "a")
    new.write(str(file1))
    new.write(str(file2))


concatenateFiles()
