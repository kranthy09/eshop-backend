"""
Serializers for Core App Models
"""

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import (
    User,
    Product,
    Brand,
    Category,
    Variant,
    Specification,
    Compatibility,
    DeliveryTimeStatus,
    Faq,
    Carousel,
    Image,
)


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


class ImageSerializer(serializers.ModelSerializer):
    """Response model for Image"""

    class Meta:
        model = Image
        fields = ("url",)


class ProductSerializer(serializers.ModelSerializer):
    """Response model for Product"""

    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class VariantSerializer(serializers.ModelSerializer):
    """Response model for Variant"""

    product = ProductSerializer()

    class Meta:
        model = Variant
        fields = "__all__"


class SpecificationSerializer(serializers.ModelSerializer):
    """Response model for Specification"""

    product = ProductSerializer()

    class Meta:
        model = Specification
        fields = "__all__"


class CompatibilitySerializer(serializers.ModelSerializer):
    """Response model for Compatibility"""

    product = ProductSerializer()

    class Meta:
        model = Compatibility
        fields = "__all__"


class DeliveryTimeStatusSerializer(serializers.ModelSerializer):
    """Response model for DeliveryTimeStatus"""

    product = ProductSerializer()

    class Meta:
        model = DeliveryTimeStatus
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    """Response model for Faq"""

    product = ProductSerializer()

    class Meta:
        model = Faq
        fields = "__all__"


class CarouselSerializer(serializers.ModelSerializer):
    """Response model for Carousel"""

    product = ProductSerializer()

    class Meta:
        model = Carousel
        fields = "__all__"


# router'Products' response serializers

# /product-detail/{id}


class ProductVaraintSerializer(serializers.ModelSerializer):
    """Response model for varaint in product detail view."""

    images = ImageSerializer(many=True)

    class Meta:
        model = Variant
        fields = ("id", "name", "price", "color", "stock", "size", "images")


class ProductSpecificationSerializer(serializers.ModelSerializer):
    """Response model for specification in product detail view."""

    class Meta:
        model = Specification
        fields = (
            "name",
            "value",
        )


class ProductCompatibilitySerializer(serializers.ModelSerializer):
    """Response model for compatibility in product detail view."""

    class Meta:
        model = Compatibility
        fields = ("name", "product_type")


class ProductDeliveryTimeStatusSerializer(serializers.ModelSerializer):
    """Response model for delivery time status in product detail view."""

    class Meta:
        model = DeliveryTimeStatus
        fields = (
            "shipping_cost",
            "estimated_delivery_time",
            "additional_info",
        )


class ProductFaqSerializer(serializers.ModelSerializer):
    """Response model for FAQ in product detail view."""

    class Meta:
        model = Faq
        fields = ("question", "answer")


class ProductCarouselSerializer(serializers.ModelSerializer):
    """Response model for Carousel in product detail view."""

    class Meta:
        model = Carousel
        fields = ("image", "title", "description")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Response model for ProductDetail"""

    category = CategorySerializer()
    brand = BrandSerializer()
    variants = ProductVaraintSerializer(many=True)
    specifications = ProductSpecificationSerializer(many=True)
    compatibility = ProductCompatibilitySerializer(many=True)
    delivery_time_status = ProductDeliveryTimeStatusSerializer()
    faqs = ProductFaqSerializer(many=True)
    carousel = ProductCarouselSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
