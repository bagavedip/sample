from django.contrib import admin
from myclientapp.models import SweetType


@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
