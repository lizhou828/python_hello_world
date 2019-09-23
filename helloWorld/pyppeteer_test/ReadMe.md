# pyppeteer
    之所以要采用谷歌chrome官方无头框架puppeteer的python版本pyppeteer，是因为有些网页是可以检测到是否是使用了selenium。并且selenium所谓的保护机制不允许跨域cookies保存以及登录的时候必须先打开网页然后后加载cookies再刷新的方式很不友好
    pyppeteer这个项目是非官方的，是基于谷歌官方puppeteer的python版本。
    注意：本来chrome就问题多多，puppeteer也是各种坑，加上pyppeteer是基于前者的改编python版本，也就是产生了只要前两个有一个有bug，那么pyppeteer就会原封不动的继承下来，本来这没什么，但是现在遇到的问题就是pyppeteer这个项目从18年9月份之后就没更新过了，前两者都在不断的更新迭代，而pyppeteer一直不更新，导致很多bug根本没人修复。
    
    
# 为啥用它
    我曾经用selenium + chrome 实现了模拟登陆某些电商平台，但是实在是有些麻烦，绕过对webdriver的检测不难，
    但是，通过webdriver对浏览器的每一步操作都会留下特殊的痕迹，会被平台识别，
    这个必须通过重新编译chrome的webdriver才能实现，麻烦得让人想哭。
    不说了，都是泪，所以直接用pyppeteer
![pyppeteer隐藏webdriver标记](./pyppeteer隐藏webdriver标记.png)


# 环境要求
    Pyppeteer requires python 3.6+.

        
# 安装第三方库
    pip install -i https://pypi.douban.com/simple pyppeteer
       
    
# 常见问题：
    1、运行pip install pyppeteer后 如报错： Command "python setup.py egg_info" failed with error code 1 in xxxx....
        则需要更新pip ,命令如下：
        python -m pip install --upgrade pip

    2、第一次运行代码时，会下载
        [W:pyppeteer.chromium_downloader] start chromium download.      
        Download may take a few minutes.  


# 参考文档
    官方文档： https://miyakogi.github.io/pyppeteer/reference.html
    网络爬虫之使用pyppeteer替代selenium完美绕过webdriver检测 http://www.manongjc.com/detail/6-lkhaqtmnlofewjs.html
    pyppeteer(python版puppeteer)基本使用 https://www.cnblogs.com/baihuitestsoftware/p/10531462.html

