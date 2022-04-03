from rest_framework import serializers
from myapp.models import Pollution_Data
class polSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pollution_Data
        fields='__all__'