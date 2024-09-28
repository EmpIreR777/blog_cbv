from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostFromCategory(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    category = None
    paginate_by = 1

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.custom.filter(category__slug=self.category.slug)
        if not queryset:
            sub_cat = Category.objects.filter(parent=self.category)
            queryset = Post.custom.filter(category__in=sub_cat)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Записи из категории: {self.category.title}'
        return context


class PostListView(ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2
    queryset = Post.custom.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная страница'
        return context


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
