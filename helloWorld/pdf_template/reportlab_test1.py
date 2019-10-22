# pip install reportlab
from reportlab.pdfgen import canvas
def hello():
    c = canvas.Canvas("reportlab_test1.pdf")
    # drawString()前两个参数，是以pdf页面左下角为原点的直角坐标系
    c.drawString(300,3,"Hello,World")

    c.showPage()
    c.save()
hello()