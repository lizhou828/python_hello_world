#简介：
    PyPI(Python Package Index)是python官方的第三方库的仓库，所有人都可以下载第三方库或上传自己开发的库到PyPI。PyPI推荐使用pip包管理器来下载第三方库。pip可正常工作在Windows、Mac OS、Unix/Linux等操作系统上，但是需要至少2.6+和搜索3.2+的CPython或PyPy的支持。python 2.7.9 和3.4以后的版本已经内置累pip程序，所以不需要安装。

#定位：

    pip是python里的包管理工具

#windows使用环境：

    在cmd输入pip <command（命令）> <安装或卸载包的名称>即可使用各种功能。

    如果你安装的Python 2 >=2.7.9 或者Python 3 >=3.4 那么Python自带了pip,所以不用安装，配置下它的环境就可以了
    路径：Python安装路径\Scripts\pip.exe



#基本使用：
    在cmd输入pip <command（命令）> <安装或卸载包的名称>即可使用各种功能。


    查看pip命令有哪些选项：pip --help

    pip的自我更新命令: pip install -U pip


    查看列出已安装的软件包 ： pip list
    查找需要更新的软件包： pip list --outdated
    搜素软件包 pip search "SomePackage"
    
    安装包：pip install SomePackage
    安装 PyPI软件包
    $ pip install SomePackage             # latest version
    $ pip install SomePackage==1.0.4      # specific version
    $ pip install 'SomePackage>=1.0.4'    # minimum version
    
    
    卸载安装包：pip uninstall SomePackage
    
    更新软件包： pip install --upgrade SomePackage

