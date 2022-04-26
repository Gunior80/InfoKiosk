from django.apps import AppConfig
from django.utils.translation import gettext as _
from InfoKiosk.settings import GRAPPELLI_ADMIN_TITLE


class CmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CMS'
    verbose_name = GRAPPELLI_ADMIN_TITLE
