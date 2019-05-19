from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = ('organization', 'fest', 'user', 'payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/organization/', include(('organization.urls', 'organization'), namespace='organization')),
    path('api/fest/', include(('fest.urls', 'fest'), namespace='fest')),
    path('api/user/', include(('user.urls', 'user'), namespace='user')),
    path('api/payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('api/blog/', include(('blog.urls','blog'), namespace='blog')),
    path('api/event/', include(('Event.urls','event'), namespace='event')),
    # path('api/file/', include(('File.urls','file'), namespace='file')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
