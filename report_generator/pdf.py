from fpdf import FPDF


class Template(FPDF):
    def __init__(self, orientation, unit, format):
        super().__init__(orientation=orientation, unit=unit, format=format)
        self.pdf_holder = ''
        self.filename = None

    def set_filename(self, filename):
        self.filename = filename

    def header(self):
        self.image('logo-dark.png', 10, 8, 33)
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()))

    def generate(self):
        self.output(self.filename)
