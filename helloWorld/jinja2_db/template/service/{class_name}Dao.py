
from {{package_name}}.DB.BaseDao import BaseDao
from {{package_name}}.model.{{class_name}} import {{class_name}}

class {{class_name}}Dao(BaseDao):

    def __init__(self):
        super().__init__({{class_name}})
        pass