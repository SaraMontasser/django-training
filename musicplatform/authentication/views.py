from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login,logout
from knox.models import AuthToken
# Create your views here.

class register(APIView):
    permission_classes = []
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    permission_classes = []
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # return Response('Session login successful.')
        return Response({
                "token": AuthToken.objects.create(user)[1],
                "user": {
                "id": user.id,
                "username":  user.username,
                "email":  user.email,
                "bio":  user.bio
            },
        })


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response('User Logged out successfully')