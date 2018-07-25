from aip import AipSpeech
import os

# 百度语音识别接口
# 不支持语义、意图识别，AndroidSDN支持语义、意图识别

#""" 你的 APPID AK SK """
APP_ID = '10293937'
API_KEY = 'rwdTiADREGfwfcj9ZaZC9sbK'
SECRET_KEY = '2c06fa850fa662018dbe40b015c0f0f6'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# localFileName = r"C:\Users\Administrator\Desktop\public\public\8k.pcm";

# 当前文件的路径
pwd = os.getcwd()
# 当前文件的父路径
father_path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
# 来自微信语音文件
localFileName = pwd + r"\file\spend_10_yuan_today_breakfast.amr"

# 识别本地文件
result = aipSpeech.asr(
                        get_file_content(localFileName),
                        'amr',
                        8000,
                        {'lan': 'zh'}
                      )
print(result)
print(type(result))

# 从URL获取文件识别
# aipSpeech.asr('', 'pcm', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
#   }
#)