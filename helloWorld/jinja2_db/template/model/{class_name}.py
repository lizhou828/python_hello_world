import json

class {{class_name}}(object):

    def __init__(self):
    {% for column in columns %}
        # {{column.comment}}
        self.__{{column.name}} = None
    {% endfor %}

    {% for column in columns %}
    def get_{{column.name}}(self):
        # {{column.comment}}
        return self.__{{column.name}}
    {% endfor %}
    {%for column in columns %}
    def set_{{column.name}}(self, {{column.name}}):
        # {{column.comment}}
        self.__{{column.name}} = {{column.name}}
    {% endfor %}

    def __str__(self):
        {{class_name}}Dict = {
            {% for column in columns %}
                {% if loop.first %}
                    '{{column.name}}': self.__{{column.name}}
                {%else%}
                    ,'{{column.name}}': self.__{{column.name}}
                {%endif%}
            {% endfor %}
        }
        return json.dumps({{class_name}}Dict)
