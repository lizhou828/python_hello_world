import json

# python对象转字典的两种方式  https://blog.csdn.net/weixin_42359464/article/details/80882549

class A(object):
    name = 'wukt'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ('name', 'age', 'gender')

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

obj_list = []
a = A()
obj_list.append(dict(a))
b = A()
obj_list.append(dict(b))
c = A()
obj_list.append(dict(c))
r = dict(a)
print(r)
print(r.get("name"))
print(r["age"])
print(obj_list)
json.dumps(obj_list)
# ————————————————
# 版权声明：本文为CSDN博主「weixin_42359464」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_42359464/article/details/80882549