import time
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Image
from reportlab.lib.units import inch


def generatePdf(fileName,imageName):
    doc = SimpleDocTemplate(fileName, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    Story = []
    logo = imageName
    im = Image(logo, 5 * inch, 5 * inch)
    Story.append(im)


    doc.build(Story)