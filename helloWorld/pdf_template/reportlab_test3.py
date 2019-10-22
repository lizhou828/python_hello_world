# pip install PyPDF2
from datetime import date

from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# 添加文本到已有的pdf文件中
pdfmetrics.registerFont(TTFont('SimSun', "simsun.ttc"))

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(100, 500, "Hello world")

textobject = can.beginText()
textobject.setTextOrigin(inch, 2*inch) # 在页面上显示的位置
textobject.setFont("SimSun",36)
textobject.setFillColor("#FF0000")
textobject.textLines("你瞅啥")
can.drawText(textobject)
can.showPage()

image = ImageReader("./slide4_chart1.png")
can.drawImage(image,0,0)






can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("reportlab_test3_template.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page

# 第一页内容合并
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


page = existing_pdf.getPage(1)
page.mergePage(new_pdf.getPage(1))
output.addPage(page)



# finally, write "output" to a real file
outputStream = open("reportlab_test3_result.pdf", "wb")
output.write(outputStream)
outputStream.close()