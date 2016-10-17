from django.db.models.aggregates import Avg
from rest_framework import serializers

from shop_rest_api.models import Review, Item


class ReviewSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review

    def get_items(self, obj):
        return obj.item.id

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


class ItemSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    total_approved_reviews = serializers.SerializerMethodField(read_only=True)
    avg_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item

    def get_total_approved_reviews(self, obj):
        return len(obj.reviews.all().filter(approved=True))

    def get_avg_rating(self, obj):
        return obj.reviews.filter(approved=True).aggregate(Avg('rating')).get('rating__avg')
