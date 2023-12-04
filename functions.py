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

# debug function
def debugD1P1():
    # Open the text file
    with open('puzzleInputExample.txt', 'r') as file:
        # Read all lines and put lines in a list
        lines = file.readlines();
        values = [];
        # Get clean string by trimming
        for line in lines:
            value = line.strip();  
            values.append(value);
        print(" ");
        pprint(values);

        # Add a variable 
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

# debug function
def D1P1():
    # Open the text file
    with open('puzzleInput.txt', 'r') as file:
        # Read all lines and put lines in a list
        lines = file.readlines();
        values = [];
        # Get clean string by trimming
        for line in lines:
            value = line.strip();  
            values.append(value);

        # Add a variable 
        sumStack = 0
        for value in values:
            calibrationValue = getStringFirstDigit(value) + getStringLastDigit(value);
            sumStack += int(calibrationValue);
        print('The sum of all of the calibration values is: ' + str(sumStack));
    return