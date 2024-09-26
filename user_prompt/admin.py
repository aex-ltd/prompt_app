from django.contrib import admin

from .models import TextPrompt, Hint


# text prompt admin 
class TextPromptAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'date']
    list_display_links = ['user', 'title', 'date']

admin.site.register(TextPrompt, TextPromptAdmin)


# hint admin 
class HintAdmin(admin.ModelAdmin):
    list_display = ['context', 'created_at', 'updated_at']

    list_display_links = ['context', 'created_at', 'updated_at']
    
admin.site.register(Hint, HintAdmin)

# class FilePromptAdmin(admin.ModelAdmin):
#     list_display = ['user','title', 'file', 'date']
#     list_display_links = ['user', 'title', 'file', 'date']

# admin.site.register(FilePrompt, FilePromptAdmin)
