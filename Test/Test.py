'''
    Glibs learrning test scripts
'''
import sys

def main(_args):
    starter()

def starter():
    #demo_print_1()
    #demo_input()
    #demo_arythmetic()
    demo_logic()

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
    print(a + b)
    print(a / b)
    print(a // b) # 3
    print(a % b) # 2
    print(a ** b) # a^b
    print(round(1/3, 4))

def demo_logic():
    print("==== Demo of logic ====")
    inp = input("Enter value: ")
    if (inp.lower() == "a"):
        print("A!")
    elif (inp.lower() == "b"):
        print("B!")
    elif (inp.lower() == "c"):
        print("C!")
    else:
        print("Something else.")




main(sys.argv)









