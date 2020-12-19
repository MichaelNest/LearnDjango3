from django.contrib import admin
from .models import Bboard, Rubric

class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'price', 'rubric')
    list_display_links = ('title', 'content', 'price')
    search_fields = ('title', 'content',)

admin.site.register(Bboard, BboardAdmin)
admin.site.register(Rubric)

# Register your models here.
