from pprint import pprint

#function for getting the first digit of a string
def getStringFirstDigit(string):
    for characters in string:
        if characters.isdigit():
            return characters;

#function for getting the last digit of a string
def getStringLastDigit(string):
    for characters in reversed(string):
        if characters.isdigit():
            return characters;

def getLinesFromTextFile(filePath):
    # Open the text file
    with open(filePath, 'r') as file:
        # Read all lines and put lines in a list
        lines = file.readlines();
        values = [];
        # Get clean string by trimming
        for line in lines:
            value = line.strip();  
            values.append(value);
    return(values)

def convertSpelledNumber(spelledNumber):
    match spelledNumber:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9
    return convertedNumber

# main function
def debugD1P1():
    # Open the text file
    with open('inputs/d1p1/puzzleInputExample.txt', 'r') as file:
        # Read all lines and put lines in a list
        lines = file.readlines();
        values = [];
        # Get clean string by trimming
        for line in lines:
            value = line.strip();  
            values.append(value);
        print(" ");
        pprint(values);

        sumStack = 0
        for value in values:
            print(" ");
            print(value);
            calibrationValue = getStringFirstDigit(value) + getStringLastDigit(value);
            print(getStringFirstDigit(value));
            print(getStringLastDigit(value));
            print(calibrationValue);
            print(" ");            
            sumStack += int(calibrationValue);
        print('The sum of all of the calibration values is: ' + str(sumStack));
    return

# main function
def D1P1():
    # Open the text file
    with open('inputs/d1p1/puzzleInput.txt', 'r') as file:
        # Read all lines and put lines in a list
        lines = file.readlines();
        values = [];
        # Get clean string by trimming
        for line in lines:
            value = line.strip();  
            values.append(value);
 
        sumStack = 0
        for value in values:
            calibrationValue = getStringFirstDigit(value) + getStringLastDigit(value);
            sumStack += int(calibrationValue);
        print('The sum of all of the calibration values is: ' + str(sumStack));
    return

# main function
def debugD1P2():
    values = getLinesFromTextFile('inputs/d1p2/puzzleInputExample.txt')
    pprint(values);
    spelledNumbers = ['one','two','three','four','five','six','seven','eight','nine'];
    counter = 1;
    convertedValues = [];
    for value in values:
        charStack = "";
        for character in value:
            charStack += character
            for spelledNumber in spelledNumbers:
                if charStack.find(spelledNumber) != -1:
                    charStack = charStack.replace(spelledNumber,str(counter));
                counter += 1;
            counter = 1;                    charStack = charStack.replace(spelledNumber,str(convertSpelledNumber(spelledNumber)));
        convertedValues.append(charStack);
    pprint(convertedValues);

    sumStack = 0
    for value in convertedValues:
        print(" ");
        print(value);
        calibrationValue = getStringFirstDigit(value) + getStringLastDigit(value);
        print(getStringFirstDigit(value));
        print(getStringLastDigit(value));
        print(calibrationValue);
        print(" ");            
        sumStack += int(calibrationValue);
    print('The sum of all of the calibration values is: ' + str(sumStack));
    return

# main function
def D1P2():
    values = getLinesFromTextFile('inputs/d1p2/puzzleInput.txt')
    spelledNumbers = ['one','two','three','four','five','six','seven','eight','nine'];
    counter = 1;
    convertedValues = [];
    for value in values:
        charStack = "";
        for character in value:
            charStack += character
            for spelledNumber in spelledNumbers:
                if charStack.find(spelledNumber) != -1:
                    charStack = charStack.replace(spelledNumber,str(counter));
                counter += 1;
            counter = 1;
        convertedValues.append(charStack);

    sumStack = 0
    for value in convertedValues:
        calibrationValue = getStringFirstDigit(value) + getStringLastDigit(value);
        sumStack += int(calibrationValue);
    print('The sum of all of the calibration values is: ' + str(sumStack));
    return