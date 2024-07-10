import jinja2
import pdfkit
import os

from typing import Tuple

cwd = os.getcwd()


# TODO: Make filename dynamic
# TODO: Add error handler here
# TODO: Specify the return type of the functions

def html_to_pdf_converter(filename: str = "generated_pdf.pdf"):
    """Used to generate a PDF document given a HTML document."""

    FILE_PATH = f'{cwd}/generated_html/{filename}'

    template_loader = jinja2.FileSystemLoader(
        f"{cwd}/templates")
    template_env = jinja2.Environment(loader=template_loader)

    basic_template = template_env.get_template("cv_revision_01.html")

    output_html_code = basic_template.render()

    if filename.split(".")[-1] != "pdf":
        return FILE_PATH

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    pdfkit.from_string(input=output_html_code,
                       output_path=FILE_PATH, configuration=config)
