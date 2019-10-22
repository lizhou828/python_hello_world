import os
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
Elements = []

doc = BaseDocTemplate('reportlab_pdf分栏.pdf', showBoundary=1)


def foot1(canvas, doc):
	canvas.saveState()
	canvas.setFont('Times-Roman', 19)
	canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
	canvas.restoreState()


def foot2(canvas, doc):
	canvas.saveState()
	canvas.setFont('Times-Roman', 9)
	canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
	canvas.restoreState()


# normal frame as for SimpleFlowDocument
frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

# 分两栏
frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width / 2 - 6, doc.height, id='col1')
frame2 = Frame(doc.leftMargin + doc.width / 2 + 6, doc.bottomMargin, doc.width / 2 - 6,
			   doc.height, id='col2')
# 设置页面模板
doc.addPageTemplates([PageTemplate(id='OneCol', frames=frameT, onPage=foot1),

					  PageTemplate(id='TwoCol', frames=[frame1, frame2], onPage=foot2),
					  ])



# 设置每一页PDF的模板，并填充内容
Elements.append(Paragraph("Frame one column, " * 5, styles['Normal']))
Elements.append(NextPageTemplate('TwoCol'))
Elements.append(PageBreak())
Elements.append(Paragraph("Frame two columns,  " * 300, styles['Normal']))
Elements.append(NextPageTemplate('OneCol'))
Elements.append(PageBreak())
Elements.append(Paragraph("Une colonne", styles['Normal']))


# 构建PDF文件
doc.build(Elements)
# use external program xpdf to view the generated pdf
# os.system("xpdf basedoc.pdf")