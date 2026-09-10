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
    #demo_logic()
    demo_cycle()
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

def demo_logic():
    print("==== Demo of logic ====")
    inp = input("Enter value: ")
    if (inp.strip().lower() == "a"):
        print("A!")
    elif (inp.strip().lower() == "b"):
        print("B!")
    elif (inp.strip().lower() == "c"):
        print("C!")
    else:
        print("Something else.")

def demo_cycle () :
    print("==== Demo cycle ====")
    for i in range(10) :
        print(i) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print ();
    for i in range(5, 10) :
        print(i) #5, 6, 7, 8, 9
    print ();
    for i in range(5, 10, 2) :
        print(i) #5, 7, 9



def test():
    print("==== Test ====")

main(sys.argv)

sys.exit() # Stops the script








