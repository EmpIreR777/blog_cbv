from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Post, Category, Comment, Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Админ-панель модели рейтинга
    """

    pass


@admin.register(Comment)
class CommentAdminPage(DjangoMpttAdmin):
    """
    Админ-панель модели комментариев
    """

    pass


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):

    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    prepopulated_fields = {'slug': ('title',)}
