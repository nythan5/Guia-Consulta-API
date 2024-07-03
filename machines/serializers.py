from rest_framework.serializers import ValidationError, ModelSerializer
from .models import Modalitie
import re


class ModalitieSerializer(ModelSerializer):
    class Meta:
        model = Modalitie
        fields = "__all__"

    # Valida se tem caracteres especiais
    def validate_name(self, value):
        if re.search(r'[^A-Za-z0-9\s]', value):
            raise ValidationError(
                "O campo 'name' não pode conter caracteres especiais.")
        return value
