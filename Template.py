'''
    Glibs learning test scripts
'''
#!/usr/bin/python3
import sys
import os
import subprocess

def main(_args):
    starter()

def starter():
    clear_console()    
    test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        



def test():
    print("==== Test ====")


main(sys.argv)

sys.exit() # Stops the script








