returnValue = ''

def listDemo(myList):
    global returnValue
    if len(myList) == 0:
        print('Invalid List')
    else:
        for i in range(len(myList)-1):
            returnValue += myList[i] + ', '
        
        returnValue += ' and ' + myList[-1]

listDemo(['Fred','Jamie','Wesley', 'Joe'])

print(returnValue)