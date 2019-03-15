from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('videoapp.urls')),
    path('', include('authentication.urls'),name="authentication")
    # path('signup/', include('authentication.urls')),
    # path('login/', include('authentication.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)