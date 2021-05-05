from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('weapons/', include('weapon.urls')),
    path('activity/', include('activity.urls')),
    path('system-site/', include('systemsite.urls')),
    path('tracking/', include('tracking.urls')),
    path('notifications/', include('notifications.urls')),
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
