from rest_framework import serializers
from .models import ViewModel

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewModel
        fields = ('id', 'user_name', 'user_surname', 'age', 'email', 'password')