
import time
import sys
import threading

def print_info(message):
    # dept = 1 表示找到该函数第一层调用者的位置信息
    # dept = 0 表示该函数定义的位置信息
    frame = sys._getframe(1)
    code = frame.f_code

    # print("func name = ", code.co_name)
    # print("func filename = ", code.co_filename)
    # print("func import lineno = ", code.co_firstlineno)  # 模块导入该函数的位置
    # print("func call lineno = ", frame.f_lineno)  # 模块调用该函数的位置
    # print("func locals = ", frame.f_locals)

    thread_name = threading.currentThread().getName()
    ident = threading.currentThread().ident
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ">>> [", thread_name, "-", ident, "] (", code.co_filename, "@", frame.f_lineno, "line)", ":", message)


print_info("内建函数id()可以查看每个对象的内存地址:")
print_info(id(2))


