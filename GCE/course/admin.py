from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Subject)
class Subject_Admin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug'
    ]
    prepopulated_fields = {'slug': ('title',)}

class AddModule(admin.StackedInline):
    model = models.Module

@admin.register(models.Course)
class Course_Admin(admin.ModelAdmin):
    list_display =[
        'title',
        'subject',
        'created',
    ]
    list_filter = ['created', 'subject']
    search_fields = ["title", 'overview']
    prepopulated_fields = {'slug':('title',)}
    inlines =[AddModule]






