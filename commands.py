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
    elif command == 'debug':
        functions.debug()    
    elif command == 'd1p1 --debug':
        functions.debugD1P1()
    elif command == 'd1p1':
        functions.D1P1()
    elif command == 'd1p2 --debug':
        functions.debugD1P2()
    elif command == 'd1p2':
        functions.D1P2()
    elif command == 'd2p1 --debug':
        functions.debugD2P1()
    elif command == 'd2p1':
        functions.D2P1()
    elif command == 'd2p2 --debug':
        functions.debugD2P2()
    elif command == 'd2p2':
        functions.D2P2()
    elif command == 'd3p1 --debug':
        functions.debugD3P1()
    elif command == 'd3p1':
        functions.D3P1()
    
    else:
        print('[ ❌ Command not found! ❌ ]');