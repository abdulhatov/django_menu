from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Menu, MenuAdmin)