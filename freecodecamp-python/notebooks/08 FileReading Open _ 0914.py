# Reading files:  Python read command - read()
# From a text file, a CSV file, or an HTML file.

# Open & Close
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
print(file.read())
file.close()
    # r = read file
    # w = write file
    # a = append file

# # readable() - boolean value to tell us if txt file can be read
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
print(file.readable())
file.close()


# readline() - read the first line
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
print(file.readline())
file.close()


# readline() *n - reading multiple lines: like moving a cursor onto the next line - read line one by one.
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
print(file.readline())
print(file.readline())
file.close()


# readlines() -  take all the lines in the file and make them array
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
print(file.readlines())   # taking each line and put them as array
file.close()

# readlines()[1] -  access specific line by refer to its index in the array
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
print(file.readlines()[3])
file.close()


# readlines() function with for loop
file = open('../samples/08 FileReading Open _ 0914.txt', 'r')
for sentence in file.readlines():    # file.readlines() is an array.
    print(sentence)
file.close()