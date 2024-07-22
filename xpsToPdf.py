import easygui as g
import os
import fitz

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def xps_to_pdf(input_xps_path, output_pdf_path):
    
    xps_document = fitz.open(input_xps_path)
    pdf_document = fitz.open()

    for page_number in range(xps_document.page_count):
        xps_page = xps_document.load_page(page_number)
        pdf_page = pdf_document.new_page(width=xps_page.rect.width, height=xps_page.rect.height)

        pix = xps_page.get_pixmap()
        pdf_page.insert_image(pdf_page.rect, pixmap=pix)

    pdf_document.save(output_pdf_path)

    xps_document.close()
    pdf_document.close()

xps = resource_path("xps.png")

browse = g.buttonbox(
	msg="pronadjite fajl koji zelite da pretvorite u PDF", 
	title="Konverzija iz xml u pdf",
    choices=["quit"],
	images=[xps]
	)

if browse=="quit":
    pass

elif browse==xps:
    path_to_file = g.fileopenbox()
    print(path_to_file)

    input_xps_path = path_to_file
    output_pdf_path = path_to_file.replace("xps","pdf")

    print(output_pdf_path)
    xps_to_pdf(input_xps_path, output_pdf_path)


pyinstaller --onefile --windowed --add-data "xps.png:." isig.py