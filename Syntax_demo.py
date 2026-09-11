'''
    Glibs learning test scripts
'''
#!/usr/bin/python3
import sys

def main(_args):
    starter()

def starter():
    #demo_print_1()
    #demo_input()
    #demo_arythmetic()
    #demo_logic_operators()
    #demo_logic_if()
    demo_logic_if_2(1) # Dynamic parameter for IF
    demo_logic_if_2("a") # Dynamic parameter for IF
    #demo_logic_sycle(4)
    #demo_logic_sycle(_case = 4) # The named parameters with different types, int or str, are supported in Python 3.10 and later.
    #demo_logic_sycle(_case = "d") # The named parameters with different types, int or str, are supported in Python 3.10 and later.
    #print(demo_function_return(1)) # The returned value can be of any type, int, str, list, dict, etc.
    #print(demo_function_return(2)) # The returned value can be of any type, int, str, list, dict, etc.
    #test()

def demo_print_1():
    print("==== Demo of 'print' ====")
    print("Hello world!")
    print(2 * 2)
    print(f"2 * 2 = {2 * 2}")
    print("123", "789", sep=" ", end=" ")
    print("456")
    path = r"D:\Python\Source"
    print(path)

def demo_input():
    print("==== Demo of console input ====")
    inp = input("Enter text: ")
    print()
    print(inp)

def demo_arythmetic():
    print("==== Demo of arythmetic ====")
    a = 7
    b = 2
    print (a + b)
    print (a / b)
    print (a // b) # 3
    print (a % b) # 2
    print (a ** b) # a^b
    print (round(1/3, 4))
    i = 0
    i += 1
    print (i)

def demo_logic_operators():
    print("==== Demo of logic operators ====")
    a = 1
    b = 2
    c = 3 
    if (a > b and b <= c):
        print("A")
    if (a != b or b == c):
        print("B")
    if ("x" in "abcxyz"):
        print("C")
    if ("X" in "abcxyz"):
        print("D")

def demo_logic_if():
    print("==== Demo of logic if ====")
    inp = input("Enter value: ")
    if (inp.strip().lower() == "a"):
        print("A!")
    elif (inp.strip().lower() == "b"):
        print("B!")
    elif (inp.strip().lower() == "c"):
        print("C!")
    else:
        print("Something else.")

def demo_logic_if_2(_cond):
    print("==== Demo of logic if dynamic parameter type ====")
    print(f"Parameter: {_cond}")
    if (_cond == "a" or _cond == 1):
        print("A!")
    elif (_cond == "b" or _cond == 2):
        print("B!")
    elif (_cond == "c" or _cond == 3):
        print("C!")
    else:
        print("Something else.")

def demo_logic_sycle(_case=1): # Dynamic parameter type, can be int or str
    print("==== Demo switch case ====")
    print(f"Parameter: {_case}")
    match _case:
        case 1 | "a":
            for i in range(10):
                print(i) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        case 2 | "b":
            for i in range(5, 10):
                    print(i) #5, 6, 7, 8, 9
        case 3 | "c":
            for i in range(5, 10, 2):
                print(i) #5, 7, 9
        case 4 | "d":
            for ch in "Hello world!":
                print(ch) #H, e, l, l, o,  , w, o, r, l, d, !
        case _:
            print("Default case")

def demo_function_return(_case=1):
    print("==== Demo switch case ====")
    print(f"Parameter: {_case}")
    match _case:
        case 1:
            return 1
        case 2:
            return "Two"
        case _:
            return "Default case"



def test():
    print("==== Test ====")

main(sys.argv)

sys.exit() # Stops the script








