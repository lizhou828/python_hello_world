# -*- coding:utf-8 -*-

from aip import AipOcr
import os


""" 读取图片： rb表示以二进制读写模式打开 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#Windows下Python程序读取中文文件
# image = get_file_content(u'C:\\Users\\Administrator\\Desktop\\无标题.png')

# os.getcwd() 得到当前工作目录，即当前Python脚本工作的目录路径
# image = get_file_content(os.getcwd()+"\images"+ r"\无标题.png")


# def getFilesFromDir():
#     returnList = [];
#     fileList = os.listdir(os.getcwd()+"\images")
#     for f in fileList:
#         if os.path.isfile(f):
#             returnList.append(f)
#         else:
#             continue
#     return fileList


def rename(fileDir,fileName ,middleName):

    # path = os.getcwd()
    # filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    # for files in filelist:  # 遍历所有文件
    #
        Olddir = os.path.join(fileDir, fileName);  # 原来的文件路径
        if os.path.isfile(Olddir):  # 如果是文件夹则跳过
            filename = os.path.splitext(fileName)[0];  # 文件名
            filetype = os.path.splitext(fileName)[1];  # 文件扩展名
            Newdir = os.path.join(fileDir, filename+"_Telephone_"+middleName + filetype);  # 新的文件路径
            os.rename(Olddir, Newdir)  # 重命名


dirPath = os.getcwd()+"\images"
fileList = os.listdir(dirPath)
print(fileList)




""" 你的 APPID AK SK """
APP_ID = '11460695'
API_KEY = 'uZnBPApbqURDfO8mB1vtGOoX'
SECRET_KEY = 'ksu26AhiugpwOwG5ARVYNHqcRQDP08BT'


def writeFile(sqlFileName, id, telephoneNum):
    with open(sqlFileName, 'a+') as f:
        content = "update agent set agent_number = '" + telephoneNum + "' where id =" + id + ";\n"
        f.write(content)


for filePath in fileList:
     if filePath.endswith(".png"):

        fileFullPath = dirPath +"\\"+ filePath
        image = get_file_content(fileFullPath)

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        result = client.basicGeneral(image);
        print(result)
        telephoneNum = result.get("words_result")[0].get("words")

        # rename(dirPath,filePath ,telephoneNum)
        sqlFileName = r"D:\github\python_project\python_hello_world\helloWorld\readTelphoneFromImages\updateTelephone.sql";

        id = 0;
        if filePath.index(".png") > 0:
            id = filePath.replace(".png","")

        writeFile(sqlFileName,id,telephoneNum)

     else:
         continue


