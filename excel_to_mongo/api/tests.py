# api/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import UserData
import pandas as pd
from io import BytesIO

class UploadExcelTest(TestCase):
    def setUp(self):
        # تنظیمات اولیه تست
        self.client = APIClient()
        self.url = reverse('upload-excel')
    
    def generate_test_excel_file(self):
        # ساخت یک فایل اکسل تست
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Phone': ['1234567890', '0987654321', '1122334455']
        }
        df = pd.DataFrame(data)
        
        # ذخیره داده‌ها در حافظه به صورت یک فایل اکسل
        excel_file = BytesIO()
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        return excel_file

    def test_upload_excel_file(self):
        # تست آپلود فایل اکسل
        excel_file = self.generate_test_excel_file()
        response = self.client.post(self.url, {'file': excel_file}, format='multipart')

        # بررسی وضعیت پاسخ
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Data imported successfully')

        # بررسی ذخیره داده‌ها در دیتابیس
        self.assertEqual(UserData.objects.count(), 3)
        self.assertEqual(UserData.objects.first().name, 'Alice')
        self.assertEqual(UserData.objects.first().phone_number, '1234567890')
