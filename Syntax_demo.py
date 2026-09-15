'''
    Glibs learning test scripts
'''
#!/usr/bin/python3
import asyncio
import datetime
#import decimal as decAll       # Sets an alias for imported module
from decimal import Decimal, ROUND_HALF_UP
import Module_demo
import os
import subprocess
import sys
import time

def main(_args):
    starter()

def starter():
    clear_console()    
    #demo_print()
    #demo_print_sys_names()
    #demo_input()
    demo_string()
    #demo_types()
    #demo_decimal()
    #demo_dates()
    #demo_variables_and_inner_functions()
    #demo_arythmetic()
    #demo_logic_operators()
    #demo_logic_if()
    #demo_logic_if_ternary()
    #demo_logic_if_2(1) # Dynamic parameter for IF
    #demo_logic_if_2("a") # Dynamic parameter for IF
    #demo_logic_sycle(4)
    #demo_logic_sycle(_case = 4) # The named parameters with different types, int or str, are supported in Python 3.10 and later.
    #demo_logic_sycle(_case = "d") # The named parameters with different types, int or str, are supported in Python 3.10 and later.
    #print(demo_function_return(1)) # The returned value can be of any type, int, str, list, dict, etc.
    #print(demo_function_return(2)) # The returned value can be of any type, int, str, list, dict, etc.
    #print(demo_a_la_ax_strfmt("Test: %1, %2!", "Text", 123)) # Dynamic parameters
    #print(demo_a_la_ax_strfmt(123, "Text", 123)) # Raises error
    #demo_module()
    #test()

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
        
def demo_print():
    print("==== Demo of 'print' ====")
    print("Hello world!")
    print(2 * 2)
    print(f"2 * 2 = {2 * 2}")
    print("123", "789", sep=" ", end=" ")
    print("456")
    path = r"D:\Python\Source" # D:\Python\Source, but D:\Python\Source\ not working, because the last backslash is an escape character, so it needs to be escaped with another backslash or use raw string.
    print(path)
    print(1); print(2); print(3) # This way is possible
    print("Value 1: {}.    Value 2: {}.    Value 3: {}.".format(1, 2, 3)) # Formatting a string

def demo_print_sys_names():
    print("==== Demo of system names ====")
    print(__name__) # Prints the name of the current module
    print(__file__) # Prints the path of the current module
    #print(__package__) # Prints the package of the current module
    print(sys.platform) # Prints the platform (e.g., win32, linux, darwin)
    print(sys.version) # Prints the Python version

def demo_input():
    print("==== Demo of console input ====")
    inp = input("Enter text: ")
    print()
    print(inp)

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
    print("aBcD".lower()) # abcd
    print("aBcD".upper()) # ABCD
    print(ord(" ")) # 32
    print(len("012345")) # 6
    print("12" in "012345667") # True
    print("ab" not in "012345667") # True


def demo_types():
    print("==== Demo of type conversion ====")
    x = 1
    y = "a"
    z = 1.11
    print(str(x) + " " + y)
    print(int(z))
    a = "123"
    b = 25
    print(int(a) + b)
    c = "1.11"
    print(float(c) + z)
    d = "4a5b6"
    #print(int(d)) # This will raise a ValueError because the string contains non-numeric characters
    print(d.isdigit()) # False, because the string contains non-numeric characters

def demo_decimal():
    print("==== Demo of decimal type ====")
    dn1 = Decimal("1.11111")
    dn2 = Decimal("1.11111")
    print(dn1 + dn2)
    dn3 = dn1 + dn2
    print(dn3)
    dn4 = dn1 * dn2
    print(dn4)
    dn5 = dn4.quantize(Decimal("1.00")) # dn4 is untouched
    print(dn4)
    print(dn5)
    print()
    print(Decimal("1.45").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print(Decimal("1.35").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print(Decimal("1.25").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print(Decimal("1.15").quantize(Decimal("1.0"))) # Not standard mathematical rounding
    print()
    print(Decimal("1.45").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.35").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.25").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.15").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print(Decimal("1.14").quantize(Decimal("1.0"), ROUND_HALF_UP)) # Standard mathematical rounding
    print()
    print(Decimal("9").sqrt())
    print(Decimal("3").sqrt())
    print(Decimal("2")**2)
    print(Decimal("1.1")**2)
    print(pow(Decimal("1.1"),2))

def demo_dates():
    print("==== Demo of decimal type ====")
    dd = datetime.date.today()
    print(dd)
    dt = datetime.datetime.today()
    print(dt)
    time.sleep(0.5) # Seconds
    dt_2 = datetime.datetime.today()
    print(dt_2 - dt)
    async def xSleep(s):
        await asyncio.sleep(s) # Seconds
    asyncio.run(xSleep(0.3))
    dt_3 = datetime.datetime.today()
    print(dt_3 - dt_2)
    dt_4 = datetime.datetime.strptime("01-01-2027 00:00:00", "%d-%m-%Y %H:%M:%S")
    print(dt_4)
    dt_5 = datetime.datetime.strptime("01-01-27 00:00:00", "%d-%m-%y %H:%M:%S")
    print(dt_5)

def demo_variables_and_inner_functions():
    print("==== Local and global variables & inner functions ====")
    s = "Hello world!"
    print("Top function before: ", s)
    def inner_1():
        s = 0
        print("Local inner 1: ", s)
    inner_1()
    print("Top function after inner 1:", s)
    def inner_2():
        global t # Refers to variable defined outside all functions (only in main script)
        nonlocal s
        s = 0
        print("Local inner 2: ", s)
    inner_2()
    print("Top function after inner 2:", s)

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
    i = 0
    i += 1
    print(i)
    print()
    print(pow(2, 3))
    print(abs(-1))
    print(min(1, 2, 3))
    print(max(1, 2, 3))

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

def demo_logic_if_dynamic_param(_cond):
    print("==== Demo of logic if dynamic parameter type ====")
    print(f"Parameter: {_cond}")
    if _cond == "a" or _cond == 1:
        print("A!")
    elif _cond == "b" or _cond == 2:
        print("B!")
    elif _cond == "c" or _cond == 3:
        print("C!")
    else:
        pass # Do nothing, just skip to the next statement

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

def demo_a_la_ax_strfmt(_template: str, *_values):
    print("==== Demo a-la Ax strfmt() ====")
    print("Parameters:")
    print(f"        Template: {_template}")
    print(f"        Values: {_values}")
    if not isinstance(_template, str):
        raise TypeError("The template parameter must be a string!")
    i = 0
    ret: str = _template
    for val in _values:
        i += 1
        ret = ret.replace(f"%{i}", str(val))
    return ret

def demo_module():
    print("==== Demo of using a module ====")
    Module_demo.print_hello()

def demo_async_io(): # Take info from Claude
    print("==== Demo async/await ====")

def demo_threading(): # Take info from Claude
    print("==== Demo async/await ====")



def test():
    print("==== Test ====")

if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








