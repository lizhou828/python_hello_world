import sys

print("Hello world! Python 3.5.1")

print("[file %s @num: %s , message: %s ]" % ( __file__, sys._getframe().f_lineno,"caonima"))
print(str(sys._getframe().f_lineno) + " hehe.")

