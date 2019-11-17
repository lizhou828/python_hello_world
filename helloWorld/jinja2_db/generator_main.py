from jinja2 import Environment, FileSystemLoader

from helloWorld.jinja2_db.generator_service import read_tables_info


def generate_file(table_info):
    '''
    生成文件
    :param body:
    :param starttime:
    :param stoptime:
    :return:
    '''
    env = Environment(loader=FileSystemLoader('./'))
    template_file_name = "template/model/{class_name}.py"
    template = env.get_template(template_file_name)
    result_file_name ="result/model/{class_name}.py".format(class_name= table_info['class_name'])
    with open(result_file_name, 'w+', encoding='utf-8') as f:
        html_content = template.render(**table_info)
        f.write(html_content)

    template_file_name = "template/service/{class_name}Dao.py"
    template = env.get_template(template_file_name)
    result_file_name ="result/service/{class_name}Dao.py".format(class_name= table_info['class_name'])
    with open(result_file_name, 'w+', encoding='utf-8') as f:
        html_content = template.render(**table_info)
        f.write(html_content)

if __name__ == "__main__":
    tables_info = read_tables_info()
    for table in tables_info:
        generate_file(table)
