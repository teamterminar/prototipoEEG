from rest_framework import serializers
from rest_framework.authtoken.admin import User

from polls.models import msg


class MesSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(many=False, slug_field='name', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='name', queryset=User.objects.all())
    class Meta:
        model = msg
        fields = '__all__'