'''
    Strings demo Glibs Python scripts
'''
#!/usr/bin/python3
import sys
import os
import subprocess

def main(_args):
    menu()

def menu():
    clear_console()    
    #demo_string()
    #demo_string_functions()
    demo_string_formatting()
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_string():
    print("==== Strings ====")
    s1 = "Test!"
    print(s1)
    s2 = 'Test!'
    print(s2)
    mls = ("123" # Multiline string
    "456")
    print(mls)
    mlt = '''Multiline text 1
Multiline text 2
Multiline text 3'''
    print(mlt)
    sa = "12345!"
    print(sa[1]) # 2
    print(sa[-2]) # 5
    print("0123456789"[2:4]) # Substring: 23 
    print("0123456789"[:3]) # Substring: 012
    print("0123456789"[7:]) # Substring: 789
    print("0" * 5 + "1") # 000001

def demo_string_functions():
    print("==== String functions ====")
    print("aBcD".lower()) # abcd
    print("aBcD".upper()) # ABCD
    print(ord(" ")) # 32
    print(chr(9)) # \t
    print(len("012345")) # 6
    print("12" in "012345667") # True
    print("ab" not in "012345667") # True
    print("  ab  ".strip()) # ab
    print("0123456789".find("23")) # 2
    print((" 0123456789 " * 5).replace("45", "abcd")) #  0123abcd6789  0123abcd6789  0123abcd6789  0123abcd6789  0123abcd6789 
    print((" 0123456789 " * 5).replace("45", "abcd", 3)) #  0123abcd6789  0123abcd6789  0123abcd6789  0123456789  0123456789 
    print(("123;456;789").split(";")) # ['123', '456', '789']
    print("; ".join(["123","456","789"])) # From list: 123; 456; 789 
    print("; ".join(("123","456","789"))) # From tuple: 123; 456; 789
    print(" ".join("0123456789")) # From sring array: 0 1 2 3 4 5 6 7 8 9
    print("12345".isnumeric()) # True
    print("1a2b3".isnumeric()) # False

def demo_string_formatting():
    print("==== String formatting ====")
    print("P1: {}. P2: {}.".format("1", "2"))
    print("P1: {0}. P2: {1}.".format("1", "2"))
    #print("P1: {1}. P2: {2}.".format("1", "2")) # Out or array range exception!
    print("P1: {0}. P2: {0}.".format("1", "2"))




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








