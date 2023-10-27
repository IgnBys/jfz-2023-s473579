import re


def openFile(fileName,hamletArray = ['H','a', 'm', 'l', 'e', 't'], hamletFullWord = r'Hamlet'):
    with open(fileName, "r", encoding="utf-8") as file:
        file_contents = file.read()
        repCounter = 0
        line = ''
        counter = 0
        checkWord = ''

        index = 0
        length = len(file_contents)
        while index < length:
            character = file_contents[index]
            line += character

            if len(checkWord) < len(hamletFullWord):
                if character == hamletArray[counter]:
                    checkWord+=character
                    counter += 1
                else:
                    checkWord = ''
                    counter = 0

            if character=='\n':
                if checkWord=='Hamlet':
                    print(line)
                line = ''
                counter = 0
                checkWord = ''

            index+=1


#
print('---------------------SHAKESPEARE.EXP--------------------------------------')
openFile('shakespeare.exp')
print('----------------------SHAKESPEARE.EXP-----------------------------------')
openFile('shakespeare.in')
print('------------------------SIMPLE.IN------------------------------------')
openFile('simple.in')
print('-----------------------SIMPLE.EXP--------------------------------------')
openFile('simple.exp')