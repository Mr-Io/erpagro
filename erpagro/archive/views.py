from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse

from rest_framework import status

from purchases.models import Invoice
from . import pdfutils 


def purchases_invoice_pdf(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    buffer = pdfutils.get(invoice)
    return FileResponse(buffer, as_attachment=True, filename="factura.pdf")
