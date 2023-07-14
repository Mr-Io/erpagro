import io
import os

from reportlab.pdfgen import canvas

def getpath(item):
    #get filename and filepath
    filename = f"{item.__class__.__name__}_2023-{item.pk}.pdf"
    filepath = os.path.join("facturas/", 'client_invoices')
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = os.path.join(filepath, filename)
    print(f"filename: {filename}")
    print(f"filepath: {filepath}")
    print(f"pdf_save_path: {pdf_save_path}")
    return pdf_save_path


def get(item):
    # return file if already created
    save_path = getpath(item)
    if os.path.isfile(save_path):
        return open(save_path, "rb")
    # if not, create, save and return it
    buffer = create_purchases_invoice(item)
    with open(save_path, "wb") as f:
        f.write(buffer.read())
    buffer.seek(0)
    return buffer

def create_purchases_invoice(invoice):
    buffer = io.BytesIO() # file-like buffer
    p = canvas.Canvas(buffer) # Create the PDF object, using the buffer as its "file."
    p.drawString(100, 100, f"Número de albaranes: {len(invoice.entrynotes.all())}")
    p.showPage() # Close the PDF object cleanly, and we're done.
    p.save()
    buffer.seek(0)
    return buffer

def create_entrynote():
    pass

def create_sales_invoice():
    pass

def create_carrier_document():
    pass