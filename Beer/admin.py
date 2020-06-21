from django.contrib import admin
from .models import Beer, Comments


class ArticleInline(admin.StackedInline):

    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):

    fields = ['mark', 'color', 'style', 'strength', 'country', 'info']
    inlines = [ArticleInline]


admin.site.register(Beer, ArticleAdmin)
# Register your models here.
