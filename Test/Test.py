'''
    Glibs learrning test scripts
'''
#!/usr/bin/python3
import sys

def main(_args):
    starter()

def starter():
    #demo_print_1()
    #demo_input()
    #demo_arythmetic()
    demo_logic_operators()
    #demo_logic_if()
    #demo_logic_sycle(4)
    #demo_cycle(4)
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

def demo_logic_sycle(_case):
    print("==== Demo switch case ====")
    match _case:
        case 1:
            for i in range(10):
                print(i) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        case 2:
            for i in range(5, 10):
                    print(i) #5, 6, 7, 8, 9
        case 3:
            for i in range(5, 10, 2):
                print(i) #5, 7, 9
        case 4:
            for ch in "Hello world!":
                print(ch) #H, e, l, l, o,  , w, o, r, l, d, !
        case _:
            print("Default case")




def test():
    print("==== Test ====")

main(sys.argv)

sys.exit() # Stops the script








