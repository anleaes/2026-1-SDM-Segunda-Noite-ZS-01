from .models import Assento
from rest_framework import serializers

class AssentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assento
        fields = '__all__'
