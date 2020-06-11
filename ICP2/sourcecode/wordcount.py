# Word count
f_input = open('sampletext.txt', 'r') # opening the file in read mode
line = f_input.readline()      # Reading the lines from the file

wordcount = {}      # Defining empty dictionary
while line != '':
    # converting the string into lower case to remove case sensitivity and splitting the string with space
    data = line.rstrip('\n').lower().split(' ')
    # print(data)
    for i in data:
        if i in wordcount.keys():  # adding the word and its counting to dictionaries
            wordcount[i] += 1
        else:
            wordcount[i] = 1

    line = f_input.readline()   # reading the next line from the file

f_output = open("output1.txt", "w")
f_output.write(str(wordcount))   # writing the dictionaries to the output file

f_output.close()  # closing the files

f_input.close()
