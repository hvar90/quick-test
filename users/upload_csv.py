# serializers.py
from rest_framework import serializers

class CsvSerializer(serializers.Serializer):
    file = serializers.FileField()

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from .serializers import CsvSerializer

class UploadCsvView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CsvSerializer(data=request.data)
        if serializer.is_valid():
            csv_file = request.FILES['file']
            reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
            header = next(reader)
            for row in reader:
                # Process each row of the CSV file
                print(row)
            return Response({"message": "CSV file uploaded and processed successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# urls.py
from django.urls import path
from .views import UploadCsvView

urlpatterns = [
    path('upload-csv/', UploadCsvView.as_view(), name='upload-csv'),
]
