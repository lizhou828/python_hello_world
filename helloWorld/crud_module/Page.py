# -*- coding:utf-8 -*-
# 分页对象

import json
import math

class Page(object):

    def __init__(self):
        self.__page = 1
        self.__total_page = 1
        self.__total_count = 0
        self.__begin = 0
        self.__limit = 10
        self.__result = []
        pass

    def get_page(self):
        return self.__page

    def set_page(self, page):
        if page > 1:
            self.__page = page

    def get_total_page(self):
        return self.__total_page

    def set_total_page(self, total_page):
        if total_page > 1:
            self.__total_page = total_page

    def get_total_count(self):
        return self.__total_count

    def set_total_count(self, total_count):
        if total_count > 0:
            self.__total_count = total_count

    def get_begin(self):
        return self.__begin

    def set_begin(self, begin):
        if begin > 0:
            self.__begin = begin

    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        if limit > 0:
            self.__limit = limit

    def get_result(self):
        return self.__result

    def set_result(self, result):
        self.__result = result

    def __str__(self):
        pageDict = {'page':self.__page,'total_page':self.__total_page,'total_count':self.__total_count,'begin':self.__begin,'limit':self.__limit,'result':self.__result}
        return json.dumps(pageDict)