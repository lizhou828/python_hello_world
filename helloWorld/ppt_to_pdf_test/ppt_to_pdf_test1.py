import comtypes.client
import os

# 原文链接：https://blog.csdn.net/proplume/article/details/79518125

def init_powerpoint():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint

def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType = 32):
    if outputFileName[-3:] != 'pdf':
        outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName,formatType)                          # formatType = 32 for ppt to pdf
    deck.Close()

def convert_files_in_folder(powerpoint, folder):
    files = os.listdir(folder)                                      #回指定文件夹包含的文件或文件夹名字的列表
    pptfiles = [f for f in files if f.endswith((".ppt",".pptx"))]   #使用循环批量转换
    for pptfile in pptfiles:
        fullpath = os.path.join(cwd,pptfile)                        #将多个路径组合后返回
        ppt_to_pdf(powerpoint, fullpath, fullpath)

if __name__ == "__main__":
    powerpoint = init_powerpoint()
    cwd = os.getcwd()  # 返回当前进程的目录
    convert_files_in_folder(powerpoint, cwd)
    powerpoint.Quit()
