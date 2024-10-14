"""
Serializers for Core App Models
"""

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Product, Brand, Category, Review, Tags


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_admin"]


class RegisterSerializer(serializers.ModelSerializer):
    """Request Body to register a new user"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]

    def create(self, validated_data):

        user = User(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class TokenObtainSerializer(serializers.Serializer):
    """Request model for returning access token information"""

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        print("password: ", password)
        user = User.objects.filter(username=username).first()
        print("User password: ", user.password)
        print(user)
        print("Checking password", user.check_password(password))
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            }
        else:
            raise serializers.ValidationError("Invalid username or password")


class UserSerializer(serializers.ModelSerializer):
    """Response model for User"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "is_admin",
        )


class ProductSerializer(serializers.ModelSerializer):
    """Response model for Product"""

    class Meta:
        model = Product
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    """Response model for brand"""

    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """Response model for category"""

    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Response model for review"""

    class Meta:
        model = Review
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    """Response model for tags"""

    class Meta:
        model = Tags
        fields = "__all__"
