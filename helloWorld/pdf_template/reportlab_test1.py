# pip install reportlab
from reportlab.pdfgen import canvas

def hello(canvas,index):
    # drawString()前两个参数，是以pdf页面左下角为原点的直角坐标系
    canvas.drawString(300,3,"Hello,World " + str(index))
    canvas.showPage() # 关闭当前页，打开新的一页

c = canvas.Canvas("reportlab_test1.pdf")
for i in range(10):
    hello(c,i)
c.save()