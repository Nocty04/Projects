from fpdf import FPDF

def main():
    generator(input("Name: "))


def generator(name):
    pdf = FPDF()
    pdf.add_page(orientation="Portrait", format="A4")
    page_width = pdf.w
    page_height = pdf.h

    pdf.set_font("helvetica", size=60)

    pdf.cell(page_width, 10, "This is Cs50", align="C")

    img_width = 210
    img_height = 297


    pdf.image("shirtificate.png", x=(page_width - img_width) / 2, y=60, w=img_width, h=img_height)

    pdf.set_font("helvetica", size=45)
    pdf.set_y(130)
    pdf.cell(page_width, 10, name, align="C")



    pdf.output("shirtificate.pdf")


main()


