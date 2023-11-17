from rest_framework import serializers
from vechiles.models import Vechiles
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username","password","email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class VechicleSerializer(serializers.ModelSerializer):

    posting_date = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Vechiles
        fields = "__all__"