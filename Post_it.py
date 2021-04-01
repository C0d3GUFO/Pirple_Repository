print ("Welcome to this simple note-take program. \n")

fileName = input ("Please insert name of the file: ")
libraryFileName = open ("LibraryFN", "a+")
libraryFileName.close()

libraryFileName = open ("LibraryFN", "r")
secondLN = []

for name in libraryFileName:
    secondLN.append (name.strip())

if fileName not in secondLN: #Checking if the file is new, if so we add a new file text.
    postIt = input ("Please write your Post: \n")
    memPost = []
    memPost.append(postIt)
    message = open (fileName, "w")
    for x in memPost:
        message.write(str(x) + "\n")
    message.close()
    libraryFileName.close()

    libraryFileName = open ("LibraryFN", "a")
    memLibraryFN = []
    memLibraryFN.append (fileName)
    for fn in memLibraryFN:
        libraryFileName.write (str(fn) + "\n")#write file name in his file.
    libraryFileName.close()
else:
    print ("The file already exist. Please choose what you want to do next: \nA) Read the file; \nB) Delete the file and start over; \nC) Append the file; \nD) Replace a single line.")

    choice = input ("Please enter your choice: ")

    if choice == "A" or choice == "a":
        readFile = open (fileName, "r")
        for x in readFile:
            print (x.strip())
        readFile.close()

    elif choice == "B" or choice == "b":
        delFile = open (fileName, "w")
        newPost = input ("Write your new Post: \n")
        memNewPost = []
        memNewPost.append(newPost)
        for x in memNewPost:
            delFile.write(x + "\n")
        delFile.close()

    elif choice == "C" or choice == "c":
        memAddPost = []
        addPost = open (fileName, "a")
        adding = input ("Please write your adding Post: \n")
        memAddPost.append(adding)
        for x in memAddPost:
            addPost.write(str(x) + "\n")
        addPost.close()

    elif choice == "D" or choice == "d":
        with open (fileName) as fp:
            line = fp.readline()
            counter = 1
            while line:
                print ("Line {}: {}".format (counter, line.strip()))
                line = fp.readline()
                counter += 1
        memFile = []
        oldFile = open (fileName, "r")
        for x in oldFile:
            memFile.append(x.strip())
        oldFile.close()

        choiceLine = input ("Please select the line to re-write: ")
        newLine = input ("Please write the new line: \n")

        memFile [int(choiceLine) -1] = newLine

        newFile = open (fileName, "w")
        for data in memFile:
            newFile.write(str(data) + "\n")
        newFile.close()
