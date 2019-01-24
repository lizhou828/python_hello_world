# -*- coding:utf-8 -*-
# 简单的用于输出信息。
import time

class Logger(object):

    def __init__(self, obj):
        self.__obj = obj
        self.__start = None
        pass

    def start(self):
        self.__start = time.time()
        pass

    def end(self):
        print("%s >>> [%s] Finished [Time consuming %dms]" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.__obj.__name__, time.time()-self.__start))
        pass

    def outSQL(self, msg, enable=True):
        """
        输出 SQL 日志：
        - @Param: msg SQL语句
        - @Param: enable 日志开关
        """
        if enable:
            print("%s >>> [%s] [SQL] %s" % (str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), self.__obj.__name__, msg))
        pass

    def outMsg(self, msg, enable=True):
        """
        输出消息日志：
        - @Param: msg 日志信息
        - @Param: enable 日志开关
        """
        if enable:
            print("%s >>> [%s] [Msg] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.__obj.__name__, msg))
        pass