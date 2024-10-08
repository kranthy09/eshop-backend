"""
URL endpoint API response views
"""

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.models import User
from core.serializers import RegisterSerializer, TokenObtainSerializer


class HealthCheckView(APIView):
    """
    Returns a health check status.
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        health_data = {
            "status": "healthy",
            "message": "The API is up and running.",
        }
        return Response(health_data, status=status.HTTP_200_OK)


class RegisterUserView(generics.CreateAPIView):
    """Register a new user"""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class TokenObtainView(APIView):
    """Return a access token to valid user"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print("request", request.data)
        serializer = TokenObtainSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                serializer.validated_data, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
