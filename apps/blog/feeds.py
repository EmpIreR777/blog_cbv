from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Post


class LatestPostFeed(Feed):
    title = 'Мой блог на Django - последние записи'
    link = '/feeds/'
    description = 'Новые записи на моём сайте'

    def items(self):
        return Post.objects.order_by('-update')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])