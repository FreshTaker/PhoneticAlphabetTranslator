"""This program takes a user's input (a word), and outputs the Phonetic Translation.
Example: INPUT = apple
OUTPUT = A as in Alfa
P as in Papa
P as in Papa
L as in Lima
E as in Echo
"""

rawInput = input('Enter Word to be Translated: ')

# Check to see if all letters
# Make all uppercase.
INPUT = rawInput.upper()

nato = open('NatoPhonetic.txt', 'r')

nato = nato.read()
nato = nato.split()

for i in INPUT:
    matchedWord = ''
    for line in nato:
        if line[0] == i:
            matchedWord = line
            print(str(i)+' as in ' + str(matchedWord))

    if matchedWord == '':
        print('\n')
