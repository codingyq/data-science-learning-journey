
# writing file: overwrite an existing file, write a new file, append onto the end of file.


# Section A: appending another line in the txt file
file = open("08 FileReading Open _ 0914.txt", "a")
file.write("Adding additional information - new entry")     # writing something in the end of the file
# now check the file it will show a new line
# Need to be careful ! Because if run twice and it will append 2 times. - without a \n

file.write("\n Adding an another information - new entry")    # add escape characters \n

file.close()





# Section B: Overwrite the entire file and only put the line in the file
# file = open("08 FileReading Open _ 0914.txt", "w")
# file.write("\n Overwriting information")
# file.close()



# Section C: create a new file

# use "w" to create a new file - txt as extension
file = open("09 Writing and Appending Files _ 0914.txt","w")
file.write("Hi, this is a new file for 09 writing file")
file.close()

# use "w" to create a new file - html as extension
file = open("09 Writing and Appending Files _ 0914.html","w")
file.write("<p>This is HTML</p>")                                # <p> paragraph - HTML language
file.close()

# writing file: overwrite an existing file, write a new file, append onto the end of file.

