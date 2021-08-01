from django.contrib import admin
from .models import Injection, Tablet, Syrup, Suppository

class InjectionAdmin(admin.ModelAdmin):
    list_display = ['created', 'name', 'price', 'updated']
    search_fields = ['created', 'name']
    list_per_page = 10

admin.site.register(Injection, InjectionAdmin)

class TabletAdmin(admin.ModelAdmin):
    list_display = ['created', 'name', 'price', 'updated']
    search_fields = ['created', 'name']
    list_per_page = 10

admin.site.register(Tablet, TabletAdmin)

class SyrupAdmin(admin.ModelAdmin):
    list_display = ['created', 'name', 'price', 'updated']
    search_fields = ['created', 'name']
    list_per_page = 10

admin.site.register(Syrup, SyrupAdmin)

class SuppositoryAdmin(admin.ModelAdmin):
    list_display = ['created', 'name', 'price', 'updated']
    search_fields = ['created', 'name']
    list_per_page = 10

admin.site.register(Suppository, SuppositoryAdmin)
