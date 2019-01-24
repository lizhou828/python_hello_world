# -*- coding:utf-8 -*-

import json

class User(object):

    def __init__(self):
        self.__user_id = None
        self.__user_name = None
        self.__user_state = None
        pass

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, id):
        self.__user_id = id

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, name):
        self.__user_name = name

    def get_user_state(self):
        return self.__user_state

    def set_user_state(self, state):
        self.__user_state = state


    def __str__(self):
        userDict = {'user_id': self.__user_id, 'user_name': self.__user_name, 'user_state': self.__user_state}
        return json.dumps(userDict)