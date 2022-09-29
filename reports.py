import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """Creates a pdf file that contains data about the flatmates, names,
    their due amount and the period of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatemate1, flatemate2, bill):
        flatemate1_pay = str(round(flatemate1.pays(bill=bill, flatemate2=flatemate2), 2))
        flatemate2_pay = str(round(flatemate2.pays(bill=bill, flatemate2=flatemate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt=" Flatmates Bill ", border=0, align="C", ln=1)

        # Insert Period and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period :", border=0)
        pdf.cell(w=230, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatemate1.name, border=0)
        pdf.cell(w=230, h=25, txt=flatemate1_pay, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatemate2.name, border=0)
        pdf.cell(w=230, h=25, txt=flatemate2_pay, border=0, ln=1)

        # Changes the directory to files, generate and open the PDF
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
