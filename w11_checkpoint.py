#For this assignment, you'll download the file books.txt that contains the names of the books in the Book of Mormon, and save it to your computer.
#Once you have the file saved to your computer, in VS Code, open the folder that contains it and create a new Python script.
#Have your program open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

with open("books.txt") as books:
    for line in books:
        book = line.strip()
        print(book)