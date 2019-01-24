# -*- coding:utf-8 -*-
# 涉及的三方库：pymysql
# pip3 install pymysql
# 通过调用Python内置的 xml.dom.minidom 对 xml 文件进行解析，获取xml内容。此类用于下面 BaseDao 获取数据库连接信息。


import sys
import re
import pymysql
import xml.dom.minidom

from xml.dom.minidom import parse

class ConfigurationParser(object):
    """
    解析xml
    - @return configDict = {"jdbcConnectionDictList":jdbcConnectionDictList,"tableList":tableList}
    """
    def __init__(self, configFilePath=None):
        if configFilePath:
            self.__configFilePath = configFilePath
        else:
            self.__configFilePath = sys.path[0] + "/config/config.xml"
        pass

    def parseConfiguration(self):
        """
        解析xml，返回jdbc配置信息以及需要生成python对象的表集合
        """
        # 解析xml文件,获取Document对象
        DOMTree = xml.dom.minidom.parse(self.__configFilePath)    # <class 'xml.dom.minidom.Document'>
        # 获取 generatorConfiguration 节点的NodeList对象
        configDOM = DOMTree.getElementsByTagName("generatorConfiguration")[0]  #<class 'xml.dom.minicompat.NodeList'>

        # 获取 jdbcConnection 节点的 property 节点集合
        jdbcConnectionPropertyList = configDOM.getElementsByTagName("jdbcConnection")[0].getElementsByTagName("property")
        # 循环 jdbcConnection 节点的 property 节点集合，获取属性名称和属性值
        jdbcConnectionDict = {}
        for property in jdbcConnectionPropertyList:
            name = property.getAttributeNode("name").nodeValue.strip().lower()
            if property.hasAttribute("value"):
                value = property.getAttributeNode("value").nodeValue
                if re.match("[0-9]",value) and name != "password" and name != "host":
                    value = int(value)
            else:
                value = property.childNodes[0].data
                if re.match("[0-9]",value) and name != "password" and name != "host":
                    value = int(value)

            if name == "charset":
                if re.match("utf-8|UTF8", value, re.I):
                    value = "utf8"
            elif name == "port":
                value = int(value)
            elif name == "creator":
                if value == "pymysql":
                    value = pymysql
            jdbcConnectionDict[name] = value
        # print(jdbcConnectionDict)
        return jdbcConnectionDict

if __name__ == "__main__":
    print(ConfigurationParser().parseConfiguration())