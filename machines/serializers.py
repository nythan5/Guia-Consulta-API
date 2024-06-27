from rest_framework import serializers
from .models import Modalitie


class ModalitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalitie
        fields = "__all__"
