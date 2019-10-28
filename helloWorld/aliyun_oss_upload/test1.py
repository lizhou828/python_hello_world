# -*- coding: utf-8 -*-
import datetime

import oss2

print(oss2.__version__)

# 1、创建存储空间
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAI4Fp6PCsntQ5ooFhFf3du', 'nY216I2NbonYV7y75qbtKTH56flM7h')

#指定bucket和Endpoint   Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'test123456788')


# 2、上传文件
# filename由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
# key是本bucket上的文件路径
year = datetime.datetime.now().year
month = datetime.datetime.now().month
upload_file_path = 'land_report/first_land/{}-{}/安装的软件.png'.format(year,month)
print(upload_file_path)
bucket.put_object_from_file(key= upload_file_path , filename='E:/安装的软件.png')

# 3、访问文件
url = bucket.sign_url('GET', upload_file_path, 100*3600)
print("文件上传成功，返回的url是:\n"+ url)
# http://test123456788.oss-cn-shenzhen.aliyuncs.com/land_report%2Ffirst_land%2F2019-10%2F%E5%AE%89%E8%A3%85%E7%9A%84%E8%BD%AF%E4%BB%B6.png?OSSAccessKeyId=LTAI4Fp6PCsntQ5ooFhFf3du&Expires=1572244135&Signature=JKN9RyhWQmBZPE3vedVWzVWPpHE%3D
# http://test123456788.oss-cn-shenzhen.aliyuncs.com/land_report%2Ffirst_land%2F2019-10%2F%E5%AE%89%E8%A3%85%E7%9A%84%E8%BD%AF%E4%BB%B6.png?OSSAccessKeyId=LTAI4Fp6PCsntQ5ooFhFf3du&Expires=1572244184&Signature=5Vhkaw%2BCAa8st2952NmQ7sLZ9WI%3D


# 4、下载文件
# <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
bucket.get_object_to_file(upload_file_path, 'E:/我是下载的安装的软件.png')



#5、删除文件
bucket.delete_object(upload_file_path)

