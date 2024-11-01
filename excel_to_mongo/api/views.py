# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .models import UserData

class UploadExcelView(APIView):
    def post(self, request):
        file = request.FILES['file']
        data = pd.read_excel(file)

        for index, row in data.iterrows():
            UserData.objects.create(
                name=row['Name'],
                phone_number=row['Phone']
            )

        return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
