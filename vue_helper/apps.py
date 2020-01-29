import os

from django.apps import AppConfig
from django.conf import settings

from vue_helper.exceptions import VueAppNotFound
from vue_helper.utils import set_production_assets_paths


class VueHelperConfig(AppConfig):
    name = 'vue_helper'

    def ready(self):
        if settings.VUE_DEV_MODE is True:
            return

        try:
            vue_dist_path = os.path.join(
                os.path.dirname(self.apps.app_configs[settings.VUE_APP_NAME].path),
                settings.VUE_APP_NAME,
                'static',
                settings.VUE_APP_DIST_DIR_NAME
            )
        except KeyError:
            raise VueAppNotFound(f"Couldn't find {settings.VUE_APP_NAME}, make sure it's added to INSTALLED_APPS")

        set_production_assets_paths(vue_dist_path=vue_dist_path)
