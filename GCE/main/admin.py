from django.contrib import admin
from . import models

"""@admin.register(models.Series)
class Series(admin.ModelAdmin):
    list_display = (
        "user",
        "series_choice"
    )"""

class DirectAnswer(admin.TabularInline):
    model = models.Answer
    extra = 4


@admin.register(models.Question)
class Question_admin(admin.ModelAdmin):
    list_display = (
        "question",
        "paper",
    )
    inlines = [DirectAnswer]

@admin.register(models.Year)
class Year_admin(admin.ModelAdmin):
    list_display=(
        "subject",
        'title',
    )



@admin.register(models.Subject)
class Subject_admin(admin.ModelAdmin):
    list_display=(
        
        "title",
        "ordinary",
        'advanced',
        "science",
        "art",
    )
    
    