import sys

from helloWorld import print_info

print_info("Hello world! Python 3.5.1")

print_info("[file %s @num: %s , message: %s ]" % ( __file__, sys._getframe().f_lineno,"caonima"))
print_info(str(sys._getframe().f_lineno) + " hehe.")

