# 阿里云oss上传（python）
    官方地址：https://www.alibabacloud.com/help/zh/doc-detail/32030.htm
## 要求
    在OSS中，操作的基本数据单元是文件（Object）。OSS Python SDK提供了丰富的文件上传方式：
        简单上传：文件最大不能超过5GB。
        追加上传：文件最大不能超过5GB。
        断点续传上传：支持并发、断点续传、自定义分片大小。大文件上传推荐使用断点续传。最大不能超过48.8TB。
        分片上传：当文件较大时，可以使用分片上传，最大不能超过48.8TB。
## 环境准备
    OSS Python SDK适用于Python 2.6、2.7、3.3、3.4、3.5版本。
    执行命令python -V查看Python版本。
    
    安装python-devel
    对于CentOS、RHEL、Fedora系统，请执行以下命令安装python-devel：
        yum install python-devel
    
    对于Debian，Ubuntu系统，请执行以下命令安装python-devel：
        apt-get install python-dev

    安装SDK
    通过pip安装： pip install oss2
    
    通过源码安装：
    从GitHub（https://github.com/aliyun/aliyun-oss-python-sdk）下载相应版本的SDK包，解压后进入目录，确认目录下有setup.py文件，
    然后执行命令如下： python setup.py install
    
    验证SDK版本  详见：https://www.alibabacloud.com/help/zh/doc-detail/85288.htm
    验证crcmod  详见：https://www.alibabacloud.com/help/zh/doc-detail/85288.htm

     