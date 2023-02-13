def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

with open(r'SampleFile.txt','r') as file:
 
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()

print( word_count(data))