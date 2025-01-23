from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'url','logo_url','description', 'created_at']
        read_only_fields = ['id', 'created_at']