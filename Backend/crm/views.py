from django.shortcuts import render
from .models import Signup,Signin
from .serializers import SignupSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
import random
# Create your views here.

@api_view(['GET','POST'])
def signup_list(request):
    message=0
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message="Login Success"
        else:
            message="Login Failure"
    return Response(message, status=200)

@api_view(['GET','POST'])
def signin_list(request):
    message = "Enter your Credentials"  # Default message

    if request.method == 'POST':
        name = request.data.get('name', '')
        password = request.data.get('password', '')

        try:
            user = Signup.objects.get(name=name, password=password)
            message = "Login Success"
        except Signup.DoesNotExist:
            # User does not exist or password is incorrect
            message="Login failed"

    return Response(message, status=200)

