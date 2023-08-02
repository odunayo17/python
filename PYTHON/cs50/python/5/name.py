import sys


if len(sys.argv) <2:
     sys.exit("Too few args")
#elif len(sys.argv) >2:
    #sys.exit("Too many args")


for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)


#pip install cowsay






"""
import sys


if len(sys.argv) <2:
     sys.exit("Too few args")
#elif len(sys.argv) >2:
    #sys.exit("Too many args")


for arg in sys.argv:
    print("hello my name is:", arg)

"""


"""
import sys


if len(sys.argv) <2:  
     print("Too few args")
elif len(sys.argv) >2:
    print("Too many args")
else:
    print("hello my name is:", sys.argv[1]) 

"""


"""
    import sys
try:
    print("hello mf my name is:", sys.argv[1])

except:
    print("Too few args")
"""



""" import sys

print("hello mf my name is:", sys.argv[1]) """