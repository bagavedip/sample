from django.contrib import admin
from myclientapp.models import Sweet


@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = ('name', )
