from fpdf import FPDF

#pdf=FPDF()
class PDF:
    def __init__(self,orientation,user_unit,size):
        self.pdf_holder=''
        self.pdf =FPDF(orientation,user_unit,size)
    def creator(self,temp):
        self.pdf.add_page(temp)
    def font_style(self,font_family,font_style,font_size):
        self.pdf.set_font(font_family,font_style,font_size)
    def writer(self,height,text):
        self.pdf.write(height,text)
    def final(self):
        self.pdf.output("demo.pdf")

