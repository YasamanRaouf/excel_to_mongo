# api/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PhoneNumber
import openpyxl

@api_view(['POST'])
def upload_excel(request):
    file = request.FILES['file']
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2, values_only=True):  # فرض اینکه ردیف اول عناوین هستند
        phone_number = PhoneNumber(number=row[0])
        phone_number.save()

    return Response(status=status.HTTP_201_CREATED)
