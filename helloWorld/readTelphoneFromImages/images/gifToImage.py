# -*- coding:utf-8 -*-
# 图片处理模块PIL
# 安装命令 ： \python_3_5_1\Scripts\pip.exe install pillow

from PIL import Image
import os

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

def getNewFileName(fileFullPath,imageType):
    pos = fileFullPath.rfind("\\")
    fileName = fileFullPath[pos+1:]
    fileName = fileName.replace(".gif",".png")
    return fileName


# 获取文件、文件所在目录
def convertImage(oldImageType, newImageType):
    dirPath = os.getcwd()
    fileList = os.listdir(dirPath)
    for filePath in fileList:
        if filePath.endswith("." + oldImageType):
            fileFullPath = dirPath + "\\" + filePath
            newFileName = getNewFileName(fileFullPath, newImageType)
            im = Image.open(fileFullPath)
            for i, frame in enumerate(iter_frames(im)):
                frame.save(newFileName, **frame.info)
        else:
            continue



oldImageType = "gif"
newImageType = "png"
convertImage(oldImageType,newImageType )
print("把"+oldImageType+"文件类型转换为"+newImageType+"文件类型完成！")
