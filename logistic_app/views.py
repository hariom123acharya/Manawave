from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage
from django.shortcuts import render
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from logistic_app.models import ContactMessage


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.serializers import ContactMessageSerializer

class ContactSubmitView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Thank you! We will get back to you soon."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def home(request):
    return render(request, 'index.html')



@csrf_exempt
def quote(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Process quote form data
        return JsonResponse({'message': 'Success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)