from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import submit_email

urlpatterns = [
    path('dashboad/', admin.site.urls),
    path("submit-email", submit_email, name="submit_email"),
    path('', include('app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
