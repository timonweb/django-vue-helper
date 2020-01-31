import os
import re
from django.conf import settings
from django.templatetags.static import static

from vue_helper.dist import vue_dist_css, vue_dist_js
from vue_helper.exceptions import VueDistIndexFileNotFound


def set_production_assets_paths(vue_dist_path):
    js, css = get_production_assets(vue_dist_path)
    vue_dist_js.update(js)
    vue_dist_css.update(css)


def get_production_assets(vue_dist_path):
    try:
        with open(os.path.join(vue_dist_path, 'index.html'), 'r') as index_file:
            return get_js_and_css_links_from_html(index_file.read())
    except FileNotFoundError as err:
        raise VueDistIndexFileNotFound(err)


def get_js_and_css_links_from_html(html: string) -> tuple:
    """
    Parse HTML document and return a tuple of javascript and css links.
    """
    js = set([alias_path(match.group(1)) for match in
              re.finditer('<script src=[\"]?(\S+.js)', html, re.MULTILINE | re.IGNORECASE)])
    css = set([alias_path(match.group(1)) for match in
               re.finditer('<link href=[\"]?(\S+.css)', html, re.MULTILINE | re.IGNORECASE)])
    return js, css


def alias_path(path):
    return static(os.path.join(settings.VUE_APP_DIST_DIR_NAME, path))
