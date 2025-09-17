from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'adopted', 'created_at')
    list_filter = ('species', 'adopted')
    search_fields = ('name', 'breed')
