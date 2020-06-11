# Word count
filename = open('sampletext.txt', 'r')
line = filename.readline()
filename_output = open('output.txt', 'w')
wordcount = {}
while line != '':
    # converting the string into lower case to remove case sensitivity and splitting the string with space
    data = line.rstrip('\n').lower().split(' ')
    # print(data)
    for i in data:
        if i in wordcount.keys():  # adding the word and counting to dictionaries
            wordcount[i] += 1
        else:
            wordcount[i] = 1

    line = filename.readline()
for i in wordcount:
    output = i + ':' + str(wordcount[i])
    print(output)
    filename_output.write(output+'\n')
filename_output.close()


