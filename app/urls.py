from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include('User.urls', namespace='user')),
    url(r'', include('cms.urls', namespace='cms')),
]
# No se que hace esto
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
