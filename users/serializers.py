from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError
import re


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    # Aqui a gente tira a o password do validade data para ter certeza que ela vai ser salva novamente criptografada
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email already exists.")
        return value

    def validate_password(self, value):

        # Mínimo de 8 caracteres
        # Pelo menos uma letra maiúscula
        # Pelo menos um número
        # Pelo menos um caractere especial

        min_lenght = 8
        if len(value) < min_lenght:
            raise ValidationError(
                f'A senha deve conter no minimo {min_lenght} caracteres.')

        if not re.search(r'[A-Z]', value):
            raise ValidationError(
                f'A senha deve conter pelo menos uma letra maiúscula.')

        if not re.search(r'[0-9]', value):
            raise ValidationError(
                f'A senha deve conter pelo menos um número.')

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValidationError(
                f'A senha deve conter pelo menos um caractere especial.')
