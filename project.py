from pathlib import Path

class Books:
    name = None
    author = None
    year = None
    genre = None
    id = None
    status = None

    def __init__(self, books):
        if Path("books.txt").exists():
            file = open("books.txt", "r")
            for i in file:
                a = i.split()
                books.append(a)
        else:
            file = open("books.txt", "w")
        file.close()


    def addbook(self, books):
        print("\n")
        print("Adding new book to fond:")
        print("Name of a book:")
        self.name = input()
        print("Author:")
        self.author = input()
        print("year:")
        self.year = input()
        print("Genre:")
        self.genre = input()
        print("ID:")
        di = input()
        for i in range(len(books)):
            if books[i][4]==di:
                print("Need unique:")
                di = input()
        self.id = di
        self.status = "untaken"
        l = [self.name, self.author, self.year, self.genre, self.id, self.status]
        books.append(l)
        file = open("books.txt", "w")
        for i in books:
            i = " ".join(i)
            file.write(i)
            file.write("\n")
            pass
        file.close()
        print("\n")

    def deletebook(self, books):
        print("Write ID of a book that you wanna delete:")
        di = input()
        index = -1
        for i in range(len(books)):
            if books[i][4]==di:
                index = i
                break

        if index==-1:
            print("There is no such a book")
            print("\n")
            return

        if books[index][5]=="untaken":
            books.pop(index)
            file = open("books.txt", "w")
            for i in books:
                i = " ".join(i)
                file.write(i)
                file.write("\n")
            file.close()
            print("\n")
        else:
            print("Book is taken by someone")

    def sortname(self, books):
        print("Write name of a book:")
        nb = input()
        nb = nb.lower()
        index = -1
        for i in range(len(books)):
            if books[i][0] == nb:
                index = i
                break

        if index==-1:
            print("There is no such a book")
            print("\n")
        else:
            print("\n")
            print("Name of a book:", books[index][0])
            print("Author of a book:", books[index][1])
            print("Year of a book:", books[index][2])
            print("Genre of a book:", books[index][3])
            print("ID of a book:", books[index][4])
            print("Status of a book:", books[index][5])
            print("\n")
        pass

    def sortauthor(self, books):
        print("Write author of a book:")
        nb = input()
        nb = nb.lower()
        index = -1
        for i in range(len(books)):
            if books[i][1]==nb:
                index = i
                break

        if index == -1:
            print("There is no such a book")
            print("\n")
        else:
            print("\n")
            print("Name of a book:", books[index][0])
            print("Author of a book:", books[index][1])
            print("Year of a book:", books[index][2])
            print("Genre of a book:", books[index][3])
            print("ID of a book:", books[index][4])
            print("Status of a book:", books[index][5])
            print("\n")
        pass

    def showallbook(self, books):
        for i in range(len(books)):
            print("\n")
            print("Name of a book:", books[i][0])
            print("Author of a book:", books[i][1])
            print("Year of a book:", books[i][2])
            print("Genre of a book:", books[i][3])
            print("ID of a book:", books[i][4])
            print("Status of a book:", books[i][5])
            print("\n")
        pass



class Reader:
    name = None
    id = None

    def __init__(self, reader):
        if Path("reader.txt").exists():
            file = open("reader.txt", "r")
            for i in file:
                i = i.split()
                reader.append(i)

        else:
            file = open("reader.txt", "w")
        file.close()
        pass

    def addreader(self, reader):
        print("Name of a reader:")
        self.name = input()
        self.name = self.name.capitalize()
        print("ID of a reader:")
        self.id = input()
        l = [self.name, self.id]
        reader.append(l)
        file = open("reader.txt", "w")
        for i in reader:
            i = " ".join(i)
            file.write(i)
            file.write("\n")
        file.close()
        pass

    def givebook(self, reader, books):
        print("Which reader are you:")
        r = input()
        r = r.capitalize()
        index1 = -1
        for i in range(len(reader)):
            if reader[i][0] == r:
                index1 = i
                break

        if index1==-1:
            print("There is no such a reader")
            print("\n")
            return

        print("Which book you want:")
        b = input()
        index2 = -1
        for i in range(len(books)):
            if books[i][0] == b:
                index2 = i
                break

        if index2 == -1:
            print("There is no such a book")
            print("\n")
            return

        if books[index2][5]=="taken":
            print("Book is taken")
            print("\n")
            return

        # we're giving the book to certain reader in a reader list
        reader[index1].append(b)
        # rewriting whole reader.txt file with new data
        file1 = open("reader.txt", "w")
        for i in reader:
            i = " ".join(i)
            file1.write(i)
            file1.write("\n")
        file1.close()

        books[index2][5] = "taken"
        file2 = open("books.txt", "w")
        for i in books:
            i = " ".join(i)
            file2.write(i)
            file2.write("\n")
        file2.close()
        pass

    def takebook(self, reader, books):
        print("Which reader are you:")
        r = input()
        r = r.capitalize()
        index1 = -1
        for i in range(len(reader)):
            if reader[i][0] == r:
                index1 = i
                break

        if index1 == -1:
            print("There is no such a reader")
            print("\n")
            return

        print("Which book to take away:")
        b = input()
        index2 = -1
        for i in range(len(books)):
            if books[i][0] == b:
                index2 = i
                break

        if index2 == -1:
            print("There is no such a book")
            print("\n")
            return

        count = 0
        for i in reader[index1]:
            if i == b:
                count = 1
                break

        if count==0:
            print("Reader dont have this book")
            print("\n")
            return
        else:
            reader[index1].remove(b)

        file1 = open("reader.txt", "w")
        for i in reader:
            i = " ".join(i)
            file1.write(i)
            file1.write("\n")
        file1.close()

        books[index2][5] = "untaken"
        file2 = open("books.txt", "w")
        for i in books:
            i = " ".join(i)
            file2.write(i)
            file2.write("\n")
        file2.close()
        pass

books = []
reader = []
book = Books(books)
readers = Reader(reader)
while True:
    print("1.Add new book into fond")
    print("2.Delete book from fond")
    print("3.Find the book")
    print("4.Show all books")
    print("5.Add new reader")
    print("6.Give a book to reader")
    print("7.Take a book back from reader")
    print("8.Show certain reader's books")
    print("9.Show list of all unique authors")
    print("10.Show list of all unique genres")
    print("11.Exit")
    print("Which action you need:")
    a = input()

    match a:
        case "1":
            book.addbook(books)
            pass
        case "2":
            book.deletebook(books)
            pass
        case "3":
            print("Sort by:")
            print("1.Name or", "2.Author")
            print("Choose: ")
            sort  = int(input())
            if sort==1:
                book.sortname(books)
            elif sort==2:
                book.sortauthor(books)
            else:
                print("Wrong number")
            pass
        case "4":
            book.showallbook(books)
            pass
        case "5":
            readers.addreader(reader)
            pass
        case "6":
            readers.givebook(reader, books)
        case "7":
            readers.takebook(reader, books)
        case "11":
            break
        case _:
            print("Need a number")
            print("\n\n")