import json
from {{package_name}}.model import DateEncoder

class {{class_name}}(object):

    def __init__(self):
    {% for column in columns %}
        # {{column.comment}}
        self.{{column.name}} = None
    {% endfor %}

    {% for column in columns %}
    def get_{{column.name}}(self):
        # {{column.comment}}
        return self.{{column.name}}
    {% endfor %}
    {%for column in columns %}
    def set_{{column.name}}(self, {{column.name}}):
        # {{column.comment}}
        self.{{column.name}} = {{column.name}}
    {% endfor %}

    def keys(self):
        '''
        当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法
        :param self:
        :return:
        '''
        return (
                   {%- for column in columns -%}
                        {%- if loop.first -%}
                            '{{column.name}}'
                        {%- else -%}
                            , '{{column.name}}'
                        {%-endif -%}
                   {%- endfor -%}
        )

    def __getitem__(self, item):
        '''
        内置方法,当对实例化对象使用dict(obj)的时候, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值
        :param self:
        :param item:
        :return:
        '''
        return getattr(self, item)

    def __str__(self):
        {{class_name}}Dict = {
            {%- for column in columns -%}
                {%- if loop.first -%}
                    '{{column.name}}': self.{{column.name}}
                {%-else-%}
                    ,'{{column.name}}': self.{{column.name}}
                {%-endif-%}
            {%- endfor -%}
        }
        return json.dumps({{class_name}}Dict,cls=DateEncoder)
