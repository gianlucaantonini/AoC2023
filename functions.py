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

#function for reading text files
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
            counter = 1;                    
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

    convertedReversedValues = [];
    for value in values:
        charStack = "";
        for character in reversed(value):
            charStack += character
            for spelledNumber in spelledNumbers:
                specularSpelledNumber = spelledNumber[::-1];
                if charStack.find(specularSpelledNumber) != -1:
                    charStack = charStack.replace(specularSpelledNumber,str(counter));
                counter += 1;
            counter = 1;
        convertedReversedValues.append(charStack[::-1]);

    
    firstDigitList = [];
    for value in convertedValues:
        firstDigitList.append(getStringFirstDigit(value))

    lastDigitList = [];
    for value in convertedReversedValues:
        lastDigitList.append(getStringLastDigit(value));

    calibrationValueList = [];
    sumStack = 0
    for firstDigit, lastDigit in zip(firstDigitList, lastDigitList):
        calibrationValue = firstDigit + lastDigit;    
        sumStack += int(calibrationValue);   
    print('The sum of all of the calibration values is: ' + str(sumStack));
    return

# main function
def debug():
    values = getLinesFromTextFile('inputs/d2p1/puzzleInputExample.txt');
    gameIndexSplitted = values[0].split(": ");
    setOfGames = gameIndexSplitted[1].split("; ");
    individualGames = setOfGames[0].split(", ");
    individualValues = individualGames[0].split(" ");
   # pprint(gameIndexSplitted);
   # pprint(setOfGames);
   # pprint(individualGames);
   # pprint(individualValues);

    gameIndexSplittedList = [];
    counterID = 1;
    sumStack = 0;
    redStack = 0;
    greenStack = 0;
    blueStack = 0;
    for value in values:
        gameIndexSplitted = value.split(": ");
        setOfGames = gameIndexSplitted[1].split("; ");
        for value in setOfGames:
            print (counterID);
            individualGames = value.split(", ");
            for value in individualGames:
                individualValues = value.split(" ");
                cubeColor = individualValues[1];
                cubeValue = individualValues[0];
                if cubeColor == "red":
                    redStack += int(cubeValue);
                if cubeColor == "green":
                    greenStack += int(cubeValue);
                if cubeColor == "blue":
                    blueStack += int(cubeValue);
                print(individualValues);
                print(cubeColor);

            print(individualGames);

            
        if (redStack <= 12) and (greenStack <= 13) and (blueStack <= 14):
            sumStack += counterID;
        counterID += 1;
        redStack = 0;
        greenStack = 0;
        blueStack = 0;




    

    print('The sum of all of the calibration values is: ' + str(sumStack));
    return

# main function
def D2P1():
    return
