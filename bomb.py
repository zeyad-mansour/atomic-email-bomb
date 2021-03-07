import os
import sys
from bomber.bomber import Bomber

# THIS CAN ONLY BE EXECUTED FROM THE COMMAND LINE (YOU MUST CALL THE PYTHON INTERPRETER)
# ARGUMENTS MUST BE PASSED AS FOLLOWS:
# 1: DO NOT INCLUDE THE SUBJECT AND BODY ARGUMENTS; INSTEAD, TEXT WILL BE GENERATED (e.g. py bomb.py "RECIEVING_EMAIL" "NUM_EMAILS")
# 2: INCLUDE ALL 5 ARGUMENTS INCLUDING THE customSubject AND BODY (e.g. py bomb.py "RECIEVING_EMAIL" "NUM_EMAILS" "SUBJECT" "BODY" )

#clears the CLI
os.system('cls' if os.name == 'nt' else 'clear')

print('''
====================================
        Atomic Email Bomber
Creator(s): zeyad-mansour & 0xmmalik
====================================
[INFO] press ctrl+C in the CLI to quit...''')

argv = sys.argv[1:len(sys.argv)]
if len(argv) not in [2, 4]:
    raise Exception("INVALID ARGUMENTS")
    sys.quit()
else:
    atomic_bomb = Bomber(argv)
    atomic_bomb.start()
