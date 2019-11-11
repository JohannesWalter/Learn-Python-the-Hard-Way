# Reading Files
# Imports function argv from module sys
# from sys import argv

# # Tells Python that I have to give it two inputs, first, the name of the script, second, the name of the file 
# script, filename = argv

# Tells Python to open the open a file and save in it in the variable txt
# txt = open(filename)

# prints a little message
# print(f"Here's your file {filename}: ")

# Prints out the read mfile content
# print(txt.read())

# # Asks once more for the file name
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()

