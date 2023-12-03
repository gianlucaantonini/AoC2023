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
        print("Resetto ELF-CLI in:");
        print("3...");
        time.sleep(1);
        print("2...");
        time.sleep(1);
        print("1...");
        time.sleep(1);
        print("💥💥💥");
        time.sleep(1);   
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
    
    else:
        print('[ ❌ Comando non trovato! ❌ ]');