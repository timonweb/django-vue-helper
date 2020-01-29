import os
import re

from django.conf import settings
from django.templatetags.static import static

from vue_helper.dist import vue_dist_css, vue_dist_js
from vue_helper.exceptions import VueDistIndexFileNotFound


def set_production_assets_paths(vue_dist_path):
    vue_dist_assets = get_production_assets(vue_dist_path)
    vue_dist_css.update(vue_dist_assets['css'])
    vue_dist_js.update(vue_dist_assets['js'])


def get_production_assets(vue_dist_path):
    try:
        with open(os.path.join(vue_dist_path, 'index.html'), 'r') as index_file:
            return parse_html_for_js_and_css_links(index_file.read())
    except FileNotFoundError as err:
        raise VueDistIndexFileNotFound(err)


def parse_html_for_js_and_css_links(html):
    parsed_js_src = set([alias_path(match.group(1)) for match in
                         re.finditer('<script src=[\"]?(\S+.js)', html, re.MULTILINE | re.IGNORECASE)])
    parsed_css_links = set([alias_path(match.group(1)) for match in
                            re.finditer('<link href=[\"]?(\S+.css)', html, re.MULTILINE | re.IGNORECASE)])
    return {
        'js': parsed_js_src,
        'css': parsed_css_links
    }


def alias_path(path):
    return static(os.path.join(*settings.VUE_APP_DIST_DIR_NAME.split('/'), *path.split('/')))
