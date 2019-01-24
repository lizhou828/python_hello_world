# -*- coding:utf-8 -*-

import json

class User(object):

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__status = None
        pass

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


    def __str__(self):
        userDict = {'id':self.__id,'name':self.__name,'status':self.__status}
        return json.dumps(userDict)