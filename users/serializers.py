from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name="snippet-detail")

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "is_staff", "snippets"]
