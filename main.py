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
    time.sleep(0.7);
    print('⚙ ...Caricamento meccanismi elfici... ⚙');
    time.sleep(2);
    os.system('clear');
    time.sleep(0.3);
    print('[ 🧝🏻‍♀️ Benvenuto nella ELF-CLI! 🎄 ]');
    time.sleep(0.3);
    print(asciiLogo);
    time.sleep(0.1);
    print('[ 🌨  Strumento industriale per la riparazione della produzione della neve. ]')

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