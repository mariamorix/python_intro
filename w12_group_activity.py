# Download the file: books_and_chapters.txt and save it to a folder for your project. 
# Then, open that folder in VS Code and create a Python script to read through the file line by line.
# Take a minute to look at the file, understand the type of data it contains, and what character you'll need to split on to separate it into the proper pieces.

books = []
chapters = []
scriptures = []
m_chapters = []
largest_chapter = None
max_chapter = ""
max_book = ""


keep = "yes"

while keep.lower() == "yes": 
    learn = input("Which volume of scriptures they would like to learn about? ")
    with open ("books_and_chapters.txt") as data :
        for line in data:

            clean_line = line.strip()
            each_line = clean_line.split(":")
            book = each_line[0]
            chapter = int(each_line[1])
            scripture = each_line[2]

            chapters.append(chapter)
            largest_chapter = max(chapters)

            # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")

            if largest_chapter == chapter :
                max_chapter = scripture
                max_book = book

        # print(f"The largest chapter is: {largest_chapter} from Scripture: {max_chapter} and Book: {max_book}")
        
            if scripture.lower() == learn :
                m_book = book
                m_chapter = chapter
                m_chapters.append(m_chapter)
                largest_m = max(m_chapters)

                if largest_m == m_chapter :
                    max_m_book = book
        print(f"The largest chapter from {learn.capitalize()} is: {max_m_book} with {largest_m} chapters.")
    keep = input("Would like to make a new search? ")

print("See you later!")     