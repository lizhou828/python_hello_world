# selenium 自动化测试（Firefox版）

## 准备工作
    1、安装Python和Selenium包(-U参数会将已经安装的旧版更新至新版): 
    pip3 install -U selenium
    如果是win10系统下，请以管理员的方式打开cmd，再执行安装包的命令：pip3 install -U selenium
    
    2、3.0以上版本的selenium调用firefox的时候要用geckodriver.exe的才行，将这个文件放到 Python安装目录下的\Scripts目录下就行
    https://github.com/mozilla/geckodriver/releases
    
    3、安装浏览器插件Selenium IDE，以火狐浏览器为例：
    火狐浏览器安装firebug：www.firebug.com，调试所有网站语言，调试功能
    Selenium IDE 是嵌入到Firefox 浏览器中的一个插件，实现简单的浏览器操 作的录制与回放功能，IDE 录制的脚本可以可以转换成多种语言，从而帮助我们快速的开发脚本，下载地址：https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/
    
    如何使用IDE录制脚本：点击seleniumIDE——点击录制——开始录制——录制完成后点击文件Export Test Case——python/unittest/Webdriver——保存；

     
    4、PyCharm有两个版本：社区版和专业版，社区版是免费的，可以下载使用；
    在使用PyCharm时，需要配置Python的解释器，我们选择支持selenium的Python版本解释器；
    
    5、创建一个引用Selenium WebDriver Client library的Python脚本，使用Selenium WebDriver提供的类和方法模拟用户与浏览器的交互；
    