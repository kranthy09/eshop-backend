"""
URL endpoint API response views
"""

from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.models import User, Category, Brand, Product
from core.serializers import (
    RegisterSerializer,
    UserSerializer,
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    ProductDetailSerializer,
)


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


class ProfileView(APIView):
    """Return a user profile"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CategoryListAPIView(APIView):
    """
    API endpoint for managing categories.
    """

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    """
    API endpoint for managing a single category.
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Category.MultipleObjectsReturned:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandListAPIView(APIView):
    """
    API endpoint for managing brands.
    """

    def get(self, request, *args, **kwargs):

        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetailAPIView(APIView):
    """
    API endpoint for managing a single brand.
    """

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Brand.MultipleObjectsReturned:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk, *args, **kwargs):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):

        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_205_RESET_CONTENT
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):

        brand = Brand.objects.get(pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandPartialUpdateAPIView(GenericAPIView, UpdateModelMixin):
    """
    API endpoint for updating a single brand.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ProductAPIViewset(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
