
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
def disk_report():
    p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
#   print p.stdout.readlines()
    return p.stdout.readlines()

def create_pdf(input, output="reportlab_test2.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 1*inch) # 在页面上显示的位置
    textobject.textLines('''Disk Capcity Report: %s''' %date)
    for line in input:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.showPage()
    c.save()
report = disk_report()
create_pdf(report)