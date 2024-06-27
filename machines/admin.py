from django.contrib import admin
from .models import Modalitie

# Register your models here.


@admin.register(Modalitie)
class ModalitiesAdm(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_create', 'created_at',)
    search_fields = ('name',)
