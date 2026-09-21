'''
    Glibs learning test scripts
'''
#!/usr/bin/python3
import sys
import os
import subprocess

def main(_args):
    menu()

def menu():
    clear_console()    
    #demo_logic_operators()
    demo_logic_if()
    #demo_logic_if_ternary()
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_logic_operators():
    print("==== Demo of logic operators ====")
    a = 1
    b = 2
    c = 3 
    if a > b and b <= c:
        print("A")
    if a != b or b == c:
        print("B")
    if a != b or not(b == c):
        print("C")
    if "x" in "abcxyz":
        print("D")
    if "X" in "abcxyz":
        print("E")

def demo_logic_if():
    print("==== Demo of logic if ====")
    inp = input("Enter value: ")
    if inp.strip().lower() == "a":
        print("A!")
    elif inp.strip().lower() == "b":
        print("B!")
    elif inp.strip().lower() == "c":
        print("C!")
    else:
        print("Something else.")

def demo_logic_if_ternary(): # Ternary operator
    print("==== Demo of ternary operator ====")
    a = 1
    b = 2
    print("A") if a > b else print("B")




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








