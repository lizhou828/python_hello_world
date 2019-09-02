from PIL import Image
import urllib.request
import os
import time
from aip import AipOcr

from python_hello_world.helloWorld import print_info

class crei(object):
    '''
        国信房地产信息网
    '''

    def download_gif(self,_url):
        '''下载gif图片'''
        f = urllib.request.urlopen(_url)
        data = f.read()
        gif_code = _url[-9:-4]
        if not gif_code or len(gif_code) != 5:
            print_info("发现异常的gif_code,url=" + _url)
            return None

        # os.getcwd() 得到当前工作目录，即当前Python脚本工作的目录路径
        file_local_path = os.getcwd() + r"\gif\\" + gif_code + ".gif"
        if os.path.isfile(file_local_path):
            os.rename(file_local_path,  os.getcwd() + r"\gif\\" + gif_code + "_"+ str(int(time.time())) + ".gif" )

        with open(file_local_path, "wb") as code:
            code.write(data)
        return gif_code


    def gif_to_png(self,gif_code):
        '''
        gif图片转png
        @param gif_code:
        @return:
        '''
        file_local_path = os.getcwd() + r"\gif\\" + gif_code + ".gif"
        if not os.path.isfile(file_local_path):
            print_info("本地没有这个文件，file_local_path=" + file_local_path)
            return None

        newFileName = os.getcwd() + r"\png\\" + gif_code + ".png"
        if os.path.isfile(newFileName):
            os.rename(newFileName,  os.getcwd() + r"\png\\" + gif_code + "_"+ str(int(time.time())) + ".png" )

        im = Image.open(file_local_path)
        for i, frame in enumerate(self.__iter_frames(im)):
            frame.save(newFileName, **frame.info)

    def __iter_frames(self,im):
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

    def read_words_from_png(self,gif_code):
        png_file_path = os.getcwd() +  os.sep + 'png' + os.sep + gif_code +'.png'
        if not os.path.isfile(png_file_path):
            print_info("本地没有这个文件，png_file_path=" + png_file_path)
            return None

        image = self.get_file_content(png_file_path)
        """百度AipOcr  APPID AK SK """
        APP_ID = '11460695'
        API_KEY = 'uZnBPApbqURDfO8mB1vtGOoX'
        SECRET_KEY = 'ksu26AhiugpwOwG5ARVYNHqcRQDP08BT'

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # """ 调用通用文字识别, 图片参数为本地图片 """
        result = client.basicGeneral(image)
        print(result)

    def get_file_content(self,filePath):
        """ 读取图片： rb表示以二进制读写模式打开 """
        with open(filePath, 'rb') as fp:
            return fp.read()

    def add_white_background_color(self,gif_code):
        png_file_path = os.getcwd() + os.sep + 'png' + os.sep + gif_code + '.png'

        im = Image.open(png_file_path)
        x,y = im.size
        # 使用白色来填充背景 from：www.jb51.net
        # (alpha band as paste mask).
        p = Image.new('RGB', im.size, (255,255,255))
        p.paste(im, (0, 0, x, y), im)
        png_white_file_path = os.getcwd() + os.sep + 'png' + os.sep + gif_code + '_white.png'
        if os.path.isfile(png_white_file_path):
          os.remove(png_white_file_path)
        p.save(png_white_file_path)



if __name__ == "__main__":
    crei = crei()
    url = "http://www.crei.cn/images/num/tabzz.gif"
    gif_code = crei.download_gif(url)
    crei.gif_to_png(gif_code)
    # crei.add_white_background_color(gif_code)
    crei.read_words_from_png(gif_code)

