from django.contrib import admin
from .models import News,Tags,Source,Country

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    
    class Media:
        css = {
            'all': ('news/css/custom_ckeditor.css',)
        }

admin.site.register(News, NewsAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    
    class Media:
        css = {
            'all': ('tags/css/custom_ckeditor.css',)
        }

admin.site.register(Tags, TagsAdmin)

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    
    class Media:
        css = {
            'all': ('sources/css/custom_ckeditor.css',)
        }

admin.site.register(Source, SourceAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    
    class Media:
        css = {
            'all': ('countries/css/custom_ckeditor.css',)
        }

admin.site.register(Country, CountryAdmin)