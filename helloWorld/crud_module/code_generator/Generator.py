# -*- coding:utf-8 -*-

# 为了便于创建 user.py文件，此出提供了自动生成方法，只需要在配置文件中简单的配置数据库连接信息以及要生成的表即可生成对象的py类文件。
#
# 目前只实现了类对象文件的创建。

import sys
import re
import pymysql
import time
import os
import xml.dom.minidom

from xml.dom.minidom import parse

global _pythonPath
global _daoPath
global _servicePath
global _controllerPath

class Generator(object):
    """
    # python类生成器
    @param configDict 配置文件信息的字典对象
    """
    def __init__(self, configFilePath=None):
        if not configFilePath:
            self.__configDict = ConfigurationParser().parseConfiguration()
        else:
            if os.path.isabs(configFilePath):
                self.__configDict = ConfigurationParser(configFilePath).parseConfiguration()
            else:
                configFilePath = configFilePath.replace(".", sys.path[0])
            pass

    def run(self):
        """
        # 生成器执行方法
        """
        fieldDict = DBOperator(self.__configDict).queryFieldDict()
        PythonGenarator(self.__configDict, fieldDict).run()
        # DaoGenarator(self.__configDict).run()
        # ServiceGenarator(self.__configDict).run()
        # ControllerGenarator(self.__configDict).run()


class PythonGenarator(object):
    """
    # pyEntity文件生成类
    @param configDict 配置文件信息的字典对象
    """
    def __init__(self, configDict, fieldDict):
        self.__configDict = configDict
        self.__fieldDict = fieldDict
        self.__content = ""
        pass

    def run(self):
        """
        执行 py 类生成方法
        """
        for filePath in self.__configDict["pythonPathList"]:
            if not os.path.exists(filePath):
                os.makedirs(os.path.dirname(filePath), exist_ok=True)
            # 获取表名
            fileName = os.path.basename(filePath).split(".py")[0]
            # 表名（首字母大写）
            ClassName = fileName.capitalize()
            # 打开新建文件
            file = open(filePath, "w", encoding="utf-8")
            self.writeImport(file)                                  # 生成 import 内容
            self.writeHeader(file, ClassName)                       # 生成 class 头部内容
            self.writeInit(file, fileName, ClassName)               # 生成 class 的 init 方法
            tableDictString = self.writeGetSet(file, fileName)      # 生成 get/set 方法，并返回一个类属性的字典对象
            self.writeStr(file, fileName, tableDictString)          # 重写 class 的 str 方法
            file.write(self.__content)
            file.close()
            print("Generator --> %s" % (filePath))
        pass

    def writeImport(self,file ,importList = None):
        """
        # 写import部分
        """
        self.__content += "import json\r\n"
        pass

    def writeHeader(self, file, className, superClass = None):
        """
        # 写类头部（class ClassName(object):）
        """
        if not superClass:
            self.__content += "class %s(object):\r\n" % (className)
        else:
            self.__content += "class %s(%s):\r\n" % (className, superClass)
        pass

    def writeInit(self, file, fileName, className):
        """
        # 写类初始化方法
        """
        self.__content += "\tdef __init__(self):\n\t\t"
        for field in self.__fieldDict[fileName]:
            self.__content += "self.__%s = None\n\t\t" % (field)
        self.__content += "pass\r\n"
        pass

    def writeGetSet(self, file, fileName):
        """
        # 写类getXXX(),setXXX()方法
        @return tableDictString 表属性字典的字符串对象，用于写__str__()方法
        """
        tableDictString = ""
        i = 1
        for field in self.__fieldDict[fileName]:
            if i != len(self.__fieldDict[fileName]):
                tableDictString += "'%s':self.__%s," % (field,field)
            else:
                tableDictString += "'%s':self.__%s" % (field,field)
            Field = field.capitalize()
            self.__content += "\tdef get_%(field)s(self):\n\t\treturn self.__%(field)s\n\n\tdef set_%(field)s(self, %(field)s):\n\t\tself.__%(field)s = %(field)s\n\n" % ({"field":field})
            i += 1
        return tableDictString

    def writeStr(self, file, fileName, tableDictString):
        """
        # 重写__str__()方法
        """
        tableDictString = "{" + tableDictString + "}"
        self.__content += "\n\tdef __str__(self):\n\t\t%sDict = %s\r\t\treturn json.dumps(%sDict)\n" % (fileName, tableDictString, fileName)
        pass

class DaoGenarator(object):
    """
    # pyDao文件生成类
    @param configDict 配置文件信息的字典对象
    """
    def __init__(self, configDict):
        self.__configDict = configDict
        pass

    def run(self):
        pass

class ServiceGenarator(object):
    """
    # pyService文件生成类
    @param configDict 配置文件信息的字典对象
    """
    def __init__(self, configDict):
        self.__configDict = configDict
        pass

    def run(self):
        pass

class ControllerGenarator(object):
    """
    # pyControlelr生成类
    @param configDict 配置文件信息的字典对象
    """
    def __init__(self, configDict):
        self.__configDict = configDict
        pass

    def run(self):
        pass

class ConfigurationParser(object):
    """
    解析xml\n
    @return configDict = {"jdbcConnectionDictList":jdbcConnectionDictList,"tableList":tableList}
    """
    def __init__(self, configFilePath=None):
        if configFilePath:
            self.__configFilePath = configFilePath
        else:
            self.__configFilePath = sys.path[0] + "/generatorConfig.xml"
        self.__generatorBasePath = sys.path[0] + "/src/"
        pass

    def parseConfiguration(self):
        """
        解析xml，返回jdbc配置信息以及需要生成python对象的表集合
        """
        # 解析xml文件,获取Document对象
        DOMTree = xml.dom.minidom.parse(self.__configFilePath)    # <class 'xml.dom.minidom.Document'>
        # 获取 generatorConfiguration 节点的NodeList对象
        configDOM = DOMTree.getElementsByTagName("generatorConfiguration")[0]  #<class 'xml.dom.minicompat.NodeList'>

        # jdbcConnection 节点的 property 节点集合
        jdbcConnectionPropertyList = configDOM.getElementsByTagName("jdbcConnection")[0].getElementsByTagName("property")

        # pythonGenerator节点对象
        pythonDOM = configDOM.getElementsByTagName("pythonGenerator")[0]
        _pythonPath = self.__getGeneratorPath(pythonDOM.getAttributeNode("targetPath").nodeValue)

        # serviceGenerator 节点对象
        serviceDOM = configDOM.getElementsByTagName("serviceGenerator")[0]
        _servicePath = self.__getGeneratorPath(serviceDOM.getAttributeNode("targetPath").nodeValue)


        # pythonGenerator节点对象
        daoDOM = configDOM.getElementsByTagName("daoGenerator")[0]
        _daoPath = self.__getGeneratorPath(daoDOM.getAttributeNode("targetPath").nodeValue)

        # controllerGenerator 节点对象
        controllerDOM = configDOM.getElementsByTagName("controllerGenerator")[0]
        _controllerPath = self.__getGeneratorPath(controllerDOM.getAttributeNode("targetPath").nodeValue)

        # 循环 jdbcConnection 节点的 property 节点集合，获取属性名称和属性值
        jdbcConnectionDict = {"host":None,"user":None,"password":None,"port":3306,"database":None,"charset":"utf8"}
        for property in jdbcConnectionPropertyList:
            name = property.getAttributeNode("name").nodeValue.strip().lower()
            if property.hasAttribute("value"):
                value = property.getAttributeNode("value").nodeValue
            else:
                value = property.childNodes[0].data
            if name == "charset":
                if re.match("utf-8|UTF8", value, re.I):
                    continue
            elif name == "port":
                value = int(value)
            jdbcConnectionDict[name] = value
        # print(jdbcConnectionDict)


        pythonPathList = []
        daoPathList = []
        servicePathList = []
        controllerPathList = []

        # 获取 table 节点的集合
        tableList = []
        tableDOMList = configDOM.getElementsByTagName("table")
        for tableDOM in tableDOMList:
            table = {}
            name = tableDOM.getAttributeNode("name").nodeValue.strip().lower()
            alias = tableDOM.getAttributeNode("alias").nodeValue.strip().lower()
            if (not alias) or alias == '' :
                prefix = name
            else:
                prefix = alias
            table["tableName"] = name
            table["alias"] = alias
            tableList.append(table)


            pythonPath = "%s/%s.py" %(_pythonPath, prefix)
            pythonPathList.append(pythonPath)
            daoPath = "%s/%sDao.py" %(_daoPath, prefix)
            daoPathList.append(daoPath)
            servicePath = "%s/%sService.py" %(_servicePath, prefix)
            servicePathList.append(servicePath)
            controllerPath = "%s/%sController.py" %(_controllerPath, prefix)
            controllerPathList.append(controllerPath)

        configDict = {
                        "jdbcConnectionDict":jdbcConnectionDict,
                        "tableList":tableList,
                        "pythonPathList":pythonPathList,
                        "daoPathList":daoPathList,
                        "servicePathList":servicePathList,
                        "controllerPathList":controllerPathList
                    }
        # print(configDict)
        return configDict

    def __getGeneratorPath(self, targetPath):
        return self.__generatorBasePath + targetPath.replace(".","/")

class DBOperator(object):

    def __init__(self, configDict=None):
        if configDict == None:
            raise Exception("Error in DBOperator >>> jdbcConnectionDict is None")
        self.__configDict = configDict
        pass

    def queryFieldDict(self):
        """
        * 获取数据库表中的所有字段名
        * @ return tableDict
        """
        fieldDict = {}
        jdbcConnectionDict = self.__configDict["jdbcConnectionDict"]
        conn = pymysql.Connect(**jdbcConnectionDict)
        # 循环数据表
        for table in self.__configDict["tableList"]:
            tableName = table["tableName"]
            alias = table["alias"]
            fieldList = []
            # 获取游标
            cursor = conn.cursor()
            # 查询表的字段名称和类型
            sql = """SELECT COLUMN_NAME as name, DATA_TYPE as type
                     FROM information_schema.columns
                     WHERE table_schema = '%s' AND table_name = '%s'
                  """ % (self.__configDict["jdbcConnectionDict"]["database"], tableName)
            # 执行sql
            cursor.execute(sql)
            # 返回所有查询结果
            results = cursor.fetchall()
            # 关闭游标
            cursor.close()
            # 将表所有字段添加到 fieldList 中
            for result in results:
                field = result[0].lower()
                fieldList.append(field)
            fieldDict[alias] = fieldList
        # 关闭数据库连接
        conn.close()
        return fieldDict

if __name__ == "__main__":
    Generator().run()