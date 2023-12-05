import os
import functions
import time

asciiLogo = r''' 
███████ ██      ███████      ██████ ██      ██
██      ██      ██          ██      ██      ██ 
█████   ██      █████ █████ ██      ██      ██ 
██      ██      ██          ██      ██      ██ 
███████ ███████ ██           ██████ ███████ ██                                                                           
    ''';

def commandsLoop(command):
    #system commands
    if command == 'reset':  
        os.system("python3 main.py");
        exit();
    elif command == 'exit':
        exit();
    elif command == 'clear':
        os.system('clear');
        time.sleep(0.3);
        print(asciiLogo);
    #custom commands
    elif command == 'd1p1 --debug':
        functions.debugD1P1()
    elif command == 'd1p1':
        functions.D1P1()
    elif command == 'd1p2 --debug':
        functions.debugD1P2()
    elif command == 'd1p2':
        functions.D1P2()
    
    else:
        print('[ ❌ Command not found! ❌ ]');