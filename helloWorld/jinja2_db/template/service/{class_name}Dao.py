# 引入同一目录下的py文件（来自指定py文件下，导入该文件下的某个类）

from helloWorld.jinja2_db.result.model.{{class_name}} import {{class_name}}
from helloWorld.jinja2_db.result.service.BaseDao import BaseDao

class {{class_name}}Dao(BaseDao):

    def __init__(self):
        super().__init__({{class_name}})
        pass