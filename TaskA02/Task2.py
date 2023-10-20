# piesArray = [r'[Pp ]', 'i', 'e', 's', r'[ \t\n.,;!?]']
# pies = ['p', 'i', 'e', 's', '.']
# if pies == piesArray:
#     print('true')

def openFile(fileName,piesArray = ['[Pp ]', 'i', 'e', 's', '[ \t\n.,;!?]'], patterns = [r'[Pp ]', 'i', 'e', 's', r'[ \t\n.,;!?]']):
    with open(fileName, "r", encoding="utf-8") as file:
        for row in file:
            repCounter = 0
            counter = 0
            checkWord =[]
            for i in row:
                if i in piesArray[counter]:
                    if i != ' ' or counter != 0:
                    # print(piesArray[4])
                        checkWord+=i
                    # print(checkWord)
                        counter+=1
                    if len(checkWord) >= 5:
                        sum = 0
                        for z in checkWord:
                            if z in piesArray[sum]:
                                sum +=1
                                if sum ==4:
                                    checkWord = []
                                    counter = 0

                                    repCounter += 1  # if in one row more than one Hamlet it will write the row only once
                                    if repCounter == 1:
                                        print(row.strip())

                        # checkWord = []
                        # counter = 0
                        # repCounter+=1      #if in one row more than one Hamlet it will write the row only once
                        # if repCounter == 1:
                        #     print(row.strip())
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
