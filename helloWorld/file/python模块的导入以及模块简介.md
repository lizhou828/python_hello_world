# python模块的导入以及模块简介 https://www.cnblogs.com/wspcoding/p/5634544.html


python的模块的导入方式


#主要包括以下几种导入方式：

1、import moduels(模块名字）   #导入整个模块，这种导入方式比较占用内存
2、import moduels (模块名字)  as  XX             #这里是导入整个模块的同时给它取一个别名，因为有些模块名字比较长，用一个缩写的别名代替在下次用到它时就比较方便
3、from modules(模块名字)  import func(方法）     #从一个模块里导入方法，你要用到模块里的什么方法就从那个模块里导入那个方法，这样占用的内存就比较少
也可以用别名表示 ： from modules(模块名字)  import func(方法）as   XX
4、from package.modules   import func(方法）     #从一个包的模块里导入方法 这个方法跟上面那种基本一样，占用的内存也比较少
也可以用别名表示，from modules(模块名字)  import func(方法）as   XX