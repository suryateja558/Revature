# Exception Handling Errors

# Type Error 

x = 10
y = "hello"
try:
    print(x + y)  # TypeError
except NameError:
    print("The variable x is not defined")
except TypeError:
    print("x and y are not strings")
except:
    print("please check the logic")
finally:
    print("executed")

# Value Error

try:
    x = int(input("x:"))
    y = int(input("y:"))
    print(x + y)
except NameError:
    print("the variable x is not defined")
except TypeError:
    print("x and y are not strings")
except ValueError:
    print("please give always x and y as integer")
except:
    print("please check the logic")
finally:
    print("executed")

# NameError

try:
    print(xyz)  # changed undefined variable to xyz
except NameError:
    print("the Variable x is not defined !")
except:
    print("please check the logic !")
finally:
    print("executed")

# IndexError

try:
    l1 = [1, 2, 3, 4, 5, 6, 7]
    print(l1[10])
except NameError:
    print("the variable x is not defined")
except TypeError:
    print("x and y are not strings")
except ValueError:
    print("please give always x and y as integer")
except IndexError:
    print("please check the index is given")
finally:
    print("executed")

# KeyError 

try:
    d1 = {1: 2, 3: 4, 5: 6}
    print(d1[100])
except IndexError:
    print("please check the index is given")
except KeyError:
    print("given key is not found in the dictionary")
except:
    print("please check the logic once !")
finally:
    print("executed")

# FileNotFoundError

try:
    fp = open("sample333.txt", "r")
    print(fp.read())
except IndexError:
    print("please check the index is given")
except KeyError:
    print("given key is not found in the dictionary")
except FileNotFoundError:
    print("given file is not found !")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# ModuleNotFoundError 

try:
    import Sample33
except FileNotFoundError:
    print("given file is not found")
except ModuleNotFoundError:
    print("given module is not found")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# AttributeError 

try:
    import math
    print(math.sqqrt(20))  # Typo: sqqrt should be sqrt
except FileNotFoundError:
    print("given file is not found")
except ModuleNotFoundError:
    print("given module is not found")
except AttributeError:
    print("given method is not found")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# SyntaxError
# Note: SyntaxError cannot be caught like this in real code
print("SyntaxError example skipped due to compilation blocking")

# Arithmetic Error 

a = 10
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print("do not divide the number with zero")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# OverflowError 

import math as mt
try:
    print(mt.factorial(40))
    print(mt.exp(200000))
except ZeroDivisionError:
    print("do not divide the number with zero")
except OverflowError:
    print("please give the power value minimum")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# OSError 

import os
try:
    os.remove("sample444.txt")
except ZeroDivisionError:
    print("do not divide the number with zero")
except OSError:
    print("please check the given file is there or not")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# StopIteration 

try:
    i1 = iter([10, 20, 30, 40])
    print(next(i1))
    print(next(i1))
    print(next(i1))
    print(next(i1))
    print(next(i1))
except ZeroDivisionError:
    print("do not divide the number with zero")
except SyntaxError:
    print("print after the value assignment ")
except StopIteration:
    print("please check the given logic once !")
finally:
    print("executed")

# UnBoundLocalError 

try:
    def display():
        a1 = 10
        def display2():
            nonlocal a1
            a1 = 100
            print(a1)
        display2()
    display()
except ZeroDivisionError:
    print("do not divide the number with zero")
except UnboundLocalError:
    print("print after the value assignment ")
except:
    print("please check the given logic once !")
finally:
    print("executed")

# KeyboardInterrupt

try:
    a = int(input("a:"))
except ZeroDivisionError:
    print("do not divide the number with zero")
except KeyboardInterrupt:
    print("please check the given logic once !")
except:
    print("Unknown error occurred")
finally:
    print("executed")
