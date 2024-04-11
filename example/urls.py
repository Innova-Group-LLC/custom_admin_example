from custom_admin.views import CustomAdminView
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^admin/.*$', CustomAdminView.as_view()),
    path('custom_admin/', include('custom_admin.api.urls')),
]
