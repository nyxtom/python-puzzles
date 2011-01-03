from django.conf.urls.defaults import *
from django.views.static import serve
from django.conf import settings

urlpatterns += patterns('',
)

# Import media_url for settings based on debug
if settings.DEBUG:
    media_url = settings.MEDIA_URL
    if media_url.startswith('/'):
        media_url = media_url[1:]

    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % media_url, serve, {'document_root': settings.MEDIA_ROOT})
    )
    del(media_url, serve)
