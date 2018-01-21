from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("test_report_lab.pdf", pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                        bottomMargin=18)
#doc.pagesize = landscape(A4)
elements = []

logo = "Graph0.png"
im = Image(logo, 5 * inch, 5 * inch)
elements.append(im)

data1 = [
         ["Mapping Of Nodes",""],
         ["Id","Customer Id"],
         ["0","A00001"],
         ["1","A00002"],
         ["2","A00003"],
         ["3","A00004"],
         ["4","A00005"]]

data3 = [
         ["Agent and Integrator",""],
         ["Source Node","A00001"],
         ["Destination Node", "A00005"]]
data2 = [
    ["Edges in Transaction","","","","",""],
    ["PaymentType", "nameOrig", "OrigAmount", "nameDest","DestAmount","AmountPaid"],
    ["A", "01", "ABCD", "AAAA","1000","1000"],
    ["B", "02", "CDEF", "BBBB","1000","1000"],
    ["C", "03", "SDFSDF", "CCCC","1000","1000"],
    ["D", "04", "SDFSDF", "DDDD","1000","1000"],
    ["E", "05", "GHJGHJGHJ", "EEEE","1000","1000"],
]

# TODO: Get this line right instead of just copying it from the docs
style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                    ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                    ('VALIGN', (0, 0), (0, -1), 'TOP'),
                    ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                    ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                    ])

# Configure style and word wrap
s = getSampleStyleSheet()
s = s["BodyText"]
s.wordWrap = 'CJK'
tableData1 = [[Paragraph(cell, s) for cell in row] for row in data1]
tableData2 = [[Paragraph(cell, s) for cell in row] for row in data2]
tableData3 = [[Paragraph(cell, s) for cell in row] for row in data3]

t1 = Table(tableData1)
t2 = Table(tableData2)
t3 = Table(tableData3)

t1.setStyle(style)
t2.setStyle(style)
t3.setStyle(style)

# Send the data and build the file
elements.append(t1)
elements.append(Spacer(1, 20))
elements.append(t3)
elements.append(Spacer(1, 20))
elements.append(t2)
doc.build(elements)