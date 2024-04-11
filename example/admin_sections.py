import typing

from django.utils.translation import gettext_lazy as _

from custom_admin.api.viewset_info import AdminViewSetInfo

ADMIN_URLS: typing.List[AdminViewSetInfo] = [
    AdminViewSetInfo(
        group_slug='staff',
        title=_('staff'),
        icon='el-icon-service',
        views=[
            'custom_admin.api.views.admin_log.AdminLogAdminViewSet',
        ]
    ),
]
