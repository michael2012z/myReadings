
file_path = "../raw/pg98.txt"

allBooks = []
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()[97:15933]
    book = []
    chapter = []
    for line in lines:
        if line.startswith("Book the "):
            print(line)
            if chapter != []:
                book.append(chapter)
                chapter = []
            if book != []:
                allBooks.append(book)
                book = []
        elif line.startswith("CHAPTER "):
            print(line)
            if chapter != [] and len(chapter) > 10:
                book.append(chapter)
                chapter = []
        else:
            chapter.append(line)
    if chapter != []:
        book.append(chapter)
        chapter = []
    if book != []:
        allBooks.append(book)
        book = []
            
chapterIndex = 0
for book in allBooks:
    for chapter in book:
        chapterIndex += 1
        with open("tmp/chapter_%02d.txt" % chapterIndex, "w", encoding="utf-8") as f:
            f.write("# ")
            formattedLine = ""
            for line in chapter:
                if len(line) > 1 and line[-1] == "\n":
                    formattedLine += line[: -1] + " "
                elif len(line) == 1 and line[0] == "\n":
                    if len(formattedLine) > 0:
                        f.write(formattedLine + "\n\n")
                        formattedLine = ""
                else:
                    print("ERROR: unexpected line format:", line)