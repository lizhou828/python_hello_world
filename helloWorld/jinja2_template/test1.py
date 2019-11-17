from jinja2 import Environment, FileSystemLoader

# ————————————————
# 版权声明：本文为CSDN博主「ZONG_XP」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / zong596568821xp / article / details / 100522584


def generate_html(body, starttime, stoptime):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('templates/test1_template.html')
    with open("result/test1.html", 'w+', encoding='utf-8') as f:
        html_content = template.render(start_time=starttime,
                                       stop_time=stoptime,
                                       body=body)
        f.write(html_content)


if __name__ == "__main__":
    body = []
    result = {'cabID': 1, 'shijian': 2019, 'final_result': "正常", 'info': "无",
              'image_path': "test.jpg"}
    body.append(result)
    generate_html(body, 2019, 2019)
