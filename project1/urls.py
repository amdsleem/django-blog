from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import Home, PostDetail, CatgoryDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    url(r'^post/(?P<slug>[-\w\x20]+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^category/(?P<slug>[-\w\x20]+)/$', CatgoryDetail.as_view(), name='category'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
