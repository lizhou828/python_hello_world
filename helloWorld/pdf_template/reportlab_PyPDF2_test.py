from PyPDF2 import PdfFileWriter, PdfFileReader

new_pdf = PdfFileReader(open("reportlab_test5.pdf", "rb"))
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


page = existing_pdf.getPage(2)
page.mergePage(new_pdf.getPage(2))
output.addPage(page)

# text = existing_pdf.getPage(3).extractText()
# print("existing_pdf.getPage(3).extractText()="+text)
# page = existing_pdf.getPage(3)
# page.mergePage(new_pdf.getPage(3))
# output.addPage(page)



# finally, write "output" to a real file
outputStream = open("reportlab_PyPDF2_result.pdf", "wb")
output.write(outputStream)
outputStream.close()