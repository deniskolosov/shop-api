from rest_framework import mixins, viewsets

from shop_rest_api.models import Review, Item
from shop_rest_api.serializers import ReviewSerializer, ItemSerializer


class ReviewListCreate(mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Review.objects.all().filter(approved=True)
    serializer_class = ReviewSerializer


class ItemsList(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

