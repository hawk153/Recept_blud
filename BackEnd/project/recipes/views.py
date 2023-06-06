from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import viewsets

from .models import Dish, Category
from .serializers import DishSerializer, CategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# Swagger

schema_view = get_schema_view(
    openapi.Info(
        title="My recipes API",
        default_version='v1',
        description="Use methods below for data access",

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
