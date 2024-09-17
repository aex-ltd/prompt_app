from django.contrib import admin

from .models import TextPrompt, FilePrompt


class TextPromptAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'date']
    list_display_links = ['user', 'title', 'date']

admin.site.register(TextPrompt, TextPromptAdmin)



class FilePromptAdmin(admin.ModelAdmin):
    list_display = ['user','title', 'file', 'date']
    list_display_links = ['user', 'title', 'file', 'date']

admin.site.register(FilePrompt, FilePromptAdmin)
