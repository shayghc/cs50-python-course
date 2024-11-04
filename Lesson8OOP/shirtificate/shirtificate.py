from fpdf import FPDF


class PDF:
    """
    A class to create a PDF with a custom shirt design.

    Attributes
    ----------
    pdf : FPDF
        An instance of the FPDF class from the fpdf library.

    Methods
    -------
    __init__(self, name: str)
        Initializes the PDF with a custom shirt design.
        The shirt design includes a title, a shirt image, and the name of the person.

        Parameters
        ----------
        name : str
            The name of the person who took the course.
    """

    def __init__(self, name: str):
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        # Add a page
        self.pdf.add_page()
        # Set title font
        self.pdf.set_font("helvetica", "", 50)
        # Add title content
        self.pdf.cell(
            210,
            45,
            "CS50 Shirtificate",
            center=True,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        # Add shirt image
        self.pdf.image(
            "shirtificate.png",
            h=self.pdf.epw,
            w=self.pdf.epw,
            keep_aspect_ratio=True,
            y=70,
        )
        # Add name to shirt
        self.pdf.set_font("helvetica", "", 28)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.cell(
            210,
            170,
            f"{name} took CS50",
            center=True,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )


# Input name
name = input("Name: ")
# Create an instance of the FPDF class
pdf = PDF(name)
# Save the PDF to a file
pdf.save_pdf("shirtificate.pdf")