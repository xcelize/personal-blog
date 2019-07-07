from django.contrib import admin
from .models import Article, Category, Comment, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user', 'category', 'tag', 'slug')
    fieldsets = (('Général', {
        'fields': ('title', 'image')
    }),
     ('Contenu article', {
        'fields': ('short_description', 'content')
     }),
     ('Informations', {
         'fields': ('user', 'category', 'tag')
     })
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)