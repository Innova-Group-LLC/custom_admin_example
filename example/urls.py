from custom_admin.views import CustomAdminView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^admin/.*$', CustomAdminView.as_view()),
    path('custom_admin/', include('custom_admin.api.urls')),
]

urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
