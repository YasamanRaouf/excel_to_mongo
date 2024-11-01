# api/urls.py
from django.urls import path
from .views import UploadExcelView

urlpatterns = [
    path('upload-excel/', UploadExcelView.as_view(), name='upload-excel'),
]
