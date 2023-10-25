def openFile(fileName, ageArray = ['1', '9', '[0123456789]', '[0123456789]', ' ', 'r', '.']):
    with open(fileName, "r", encoding="utf-8") as file:
        for row in file:
            repCounter = 0
            counter = 0
            checkWord =[]
            for i in row:
                if i in ageArray[counter]:
                    checkWord+=i
                    counter +=1
                    if counter == 7:
                        repCounter+=1
                        checkWord = []
                        counter = 0
                        if repCounter == 1:
                            print(row.strip())
                else:
                    checkWord = []
                    counter = 0

print('---------------------SHAKESPEARE.EXP--------------------------------------')
openFile('polish_wiki_excerpt.exp')
print('----------------------SHAKESPEARE.EXP-----------------------------------')
openFile('polish_wiki_excerpt.in')
print('------------------------SIMPLE.IN------------------------------------')
openFile('simple.in')
print('-----------------------SIMPLE.EXP--------------------------------------')
openFile('simple.exp')
