import os
import commands
import time

asciiLogo = r''' 
███████ ██      ███████      ██████ ██      ██
██      ██      ██          ██      ██      ██ 
█████   ██      █████ █████ ██      ██      ██ 
██      ██      ██          ██      ██      ██ 
███████ ███████ ██           ██████ ███████ ██                                                                           
    ''';

#initial welcome function
def initLoop():
    os.system('clear');
    time.sleep(0.3);
    print('[ 🧝🏻‍♀️ Welcome to the ELF-CLI! 🎄 ]');
    time.sleep(0.3);
    print(asciiLogo);
    time.sleep(0.1);
    print('[ 🌨  Official snow production fixing tool. ]')

#principal loop for getting the commands from the user
def mainLoop():
    command = input('[✨] ');
    if command == '':
        restartLoop();
    commands.commandsLoop(command);
    restartLoop();

#restarting the loop
def restartLoop():
    mainLoop();

#program Flow
initLoop();
mainLoop();