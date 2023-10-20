
def openFile(fileName,hamletArray = ['H','a', 'm', 'l', 'e', 't']):
    with open(fileName, "r", encoding="utf-8") as file:
        for row in file:
            repCounter = 0
            counter = 0
            checkWord =''
            for i in row:
                if i == hamletArray[counter]:
                    checkWord+=i
                    counter+=1
                    if checkWord == 'Hamlet':
                        checkWord = ''
                        counter = 0
                        repCounter+=1      #if in one row more than one Hamlet it will write the row only once
                        if repCounter == 1:
                            print(row.strip())  #use function strip() only for readability
                else:
                    checkWord = ''
                    counter = 0
print('---------------------SHAKESPEARE.EXP--------------------------------------')
openFile('shakespeare.exp')
print('----------------------SHAKESPEARE.EXP-----------------------------------')
openFile('shakespeare.in')
print('------------------------SIMPLE.IN------------------------------------')
openFile('simple.in')
print('-----------------------SIMPLE.EXP--------------------------------------')
openFile('simple.exp')
