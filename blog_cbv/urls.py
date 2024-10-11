from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.blog.feeds import LatestPostFeed


handler403 = 'apps.blog.error.tr_handler403'
handler404 = 'apps.blog.error.tr_handler404'
handler500 = 'apps.blog.error.tr_handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feeds/latest/', LatestPostFeed(), name='latest_post_feed'),
    path('', include('apps.blog.urls')),
    path('', include('apps.accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
