# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON

#Q3 Word Triangle. 

text = input("Enter word : ")
for index in range(len(text)): 
    print(text[:index + 1])


    #or i could just do
    print("P")
    print("PY")
    print("PYT")
    print("PYTH")
    print("PYTHO")
    print("PYTHON")