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

# Day 1 Part 1
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

# Day 1 Part 1
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

# Day 1 Part 2
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

# Day 1 Part 2
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

# Day 2 Part 1
def debugD2P1():
    values = getLinesFromTextFile('inputs/d2p1/puzzleInputExample.txt');
    counterID = 1;
    sumStack = 0;
    for value in values:
        gameIndexSplitted = value.split(": ");
        setOfGames = gameIndexSplitted[1].split("; ");
        isGameValid = bool(True);
        for value in setOfGames:
            individualGames = value.split(", ");
            for value in individualGames:
                individualValues = value.split(" ");
                cubeColor = individualValues[1];
                cubeValue = individualValues[0];
                if (cubeColor == "red") and (int(cubeValue) > 12) :
                    isGameValid = bool(False);
                if (cubeColor == "green") and (int(cubeValue) > 13) :
                    isGameValid = bool(False);
                if (cubeColor == "blue") and (int(cubeValue) > 14) :
                    isGameValid = bool(False);        
        if isGameValid == bool(True):
            sumStack += counterID;
        counterID += 1;    
    print('The sum of the IDs of all possible games is: ' + str(sumStack));
    return

# Day 2 Part 1
def D2P1():
    values = getLinesFromTextFile('inputs/d2p1/puzzleInput.txt');
    counterID = 1;
    sumStack = 0;
    for value in values:
        gameIndexSplitted = value.split(": ");
        setOfGames = gameIndexSplitted[1].split("; ");
        isGameValid = bool(True);
        for value in setOfGames:
            individualGames = value.split(", ");
            for value in individualGames:
                individualValues = value.split(" ");
                cubeColor = individualValues[1];
                cubeValue = individualValues[0];
                if (cubeColor == "red") and (int(cubeValue) > 12) :
                    isGameValid = bool(False);
                if (cubeColor == "green") and (int(cubeValue) > 13) :
                    isGameValid = bool(False);
                if (cubeColor == "blue") and (int(cubeValue) > 14) :
                    isGameValid = bool(False);        
        if isGameValid == bool(True):
            sumStack += counterID;
        counterID += 1;    
    print('The sum of the IDs of all possible games is: ' + str(sumStack));
    return

# Day 2 Part 2
def debugD2P2():
    values = getLinesFromTextFile('inputs/d2p2/puzzleInputExample.txt');
    counterID = 1;
    sumStack = 0;
    for value in values:
        gameIndexSplitted = value.split(": ");
        setOfGames = gameIndexSplitted[1].split("; ");
        hiScoreRGB = [0,0,0]
        for value in setOfGames:
            individualGames = value.split(", ");
            for value in individualGames:
                individualValues = value.split(" ");
                cubeColor = individualValues[1];
                cubeValue = individualValues[0];
                if cubeColor == "red" :
                    if int(cubeValue) > int(hiScoreRGB[0]):
                        hiScoreRGB[0] = cubeValue;
                if cubeColor == "green" :
                    if int(cubeValue) > int(hiScoreRGB[1]):
                        hiScoreRGB[1] = cubeValue;
                if cubeColor == "blue" :
                    if int(cubeValue) > int(hiScoreRGB[2]):
                        hiScoreRGB[2] = cubeValue;
        power = int(hiScoreRGB[0]) * int(hiScoreRGB[1]) * int(hiScoreRGB[2]);
        sumStack += power;
        print ("Game " + str(counterID) + ":")
        print ("R: " + str(hiScoreRGB[0]));
        print ("G: " + str(hiScoreRGB[1]));
        print ("B: " + str(hiScoreRGB[2]));
        print ("Power = " + str(power));
        print ("The current Sum Stack is: " + str(sumStack));  
        print ("");      
        counterID += 1;    
    print('The sum of the power of these sets is: ' + str(sumStack));
    return

# Day 2 Part 2
def D2P2():
    values = getLinesFromTextFile('inputs/d2p2/puzzleInput.txt');
    counterID = 1;
    sumStack = 0;
    for value in values:
        gameIndexSplitted = value.split(": ");
        setOfGames = gameIndexSplitted[1].split("; ");
        hiScoreRGB = [0,0,0];
        for value in setOfGames:
            individualGames = value.split(", ");
            for value in individualGames:
                individualValues = value.split(" ");
                cubeColor = individualValues[1];
                cubeValue = individualValues[0];
                if cubeColor == "red" :
                    if int(cubeValue) > int(hiScoreRGB[0]):
                        hiScoreRGB[0] = cubeValue;
                if cubeColor == "green" :
                    if int(cubeValue) > int(hiScoreRGB[1]):
                        hiScoreRGB[1] = cubeValue;
                if cubeColor == "blue" :
                    if int(cubeValue) > int(hiScoreRGB[2]):
                        hiScoreRGB[2] = cubeValue;
        power = int(hiScoreRGB[0]) * int(hiScoreRGB[1]) * int(hiScoreRGB[2]);
        sumStack += power;    
        counterID += 1;    
    print('The sum of the power of these sets is: ' + str(sumStack));
    return

#Day3 Part1
def D3P1():
    #Iniziamo mappando lo schema dal file di testo
    with open('inputs/d3p1/puzzleInput.txt', 'r') as file:
        lines = file.readlines();
    values = [];
    for line in lines:
        value = line.strip();  
        values.append(value);    
    mappedSchematic = []
    for value in values:
        rows = []
        for character in value:
            rows.append(character)       
        mappedSchematic.append(rows)
    #Usiamo la mappa per trovare le coordinate dei numeri da controllare
    numbersToCheck = []
    locationTracker = [0,0]
    for individualList in mappedSchematic:
        numbersToCheckStack = "";
        for individualCharacter in individualList:
            if locationTracker[0] != len(individualList) -1:
                nextCharacter = mappedSchematic[locationTracker[1]][locationTracker[0]+1]
            else:
                nextCharacter = "."
            if individualCharacter.isdigit():
                numbersToCheckStack += individualCharacter;
                if nextCharacter.isdigit() == bool(False):
                    numbersToCheckStack += "," 
            locationTracker[0] += 1    
        locationTracker[0] = 0
        locationTracker[1] += 1
        preparedNTC = numbersToCheckStack[:-1]
        numbersToCheck.append(preparedNTC.split(","));
    locationTracker = [0,0]
    # Una volta ottenuta la lista dei numeri la usiamo per trovare le coordinate
    coordQueque = []
    for individualNumberList in numbersToCheck:
        for setOfNumbers in individualNumberList:
            dotPhrase = ""
            for character in str(setOfNumbers):
                dotPhrase += ".";
            x = values[locationTracker[1]].find(str(setOfNumbers));
            z = locationTracker[1];
            number = setOfNumbers;
            values[locationTracker[1]] = values[locationTracker[1]].replace(str(setOfNumbers),dotPhrase,1);
            if setOfNumbers != "":
                coordQueque.append([z,x,number]);
        locationTracker[1] += 1
    # Definiamo la lista dei simboli e la grandezza della mappa
    symbols = ["!","@","#","$","%","^","&","*","=",")","-","+","/"];
    xMapSize = len(values[0])
    zMapSize = len(values)
    finalResult = 0
    for coord in coordQueque:
        shiftValue = 0
        isValid = 0
        for number in coord[2]:
            # Definiamo le aree di collisione
            origin = [coord[0],coord[1] + shiftValue];
            right = [origin[0],origin[1] + 1];
            left = [origin[0],origin[1] - 1];
            up = [origin[0] - 1,origin[1]];
            upR = [origin[0] - 1,origin[1] + 1];
            upL = [origin[0] - 1,origin[1] - 1];
            down = [origin[0] + 1,origin[1]];
            downR = [origin[0] + 1,origin[1] + 1];
            downL = [origin[0] + 1,origin[1] - 1];
            shiftValue += 1;
            collisions = [right,left,up,down,upL,upR,downL,downR];
            for collision in collisions:
                # Evitiamo l'out of range e controlliamo le collisioni
                if (collision[0] <= zMapSize - 1) and (collision[1] <= xMapSize - 1) and (collision[0] >= 0) and (collision[1] >= 0):
                    if str(mappedSchematic[collision[0]][collision[1]]) in symbols:
                        if isValid == 0:
                            finalResult += int(coord[2]);
                            isValid += 1
    print("The sum of all of the part numbers is: " + str(finalResult));
    return