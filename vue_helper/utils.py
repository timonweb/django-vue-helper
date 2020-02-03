import logging
import os
import re

from django.conf import settings
from django.templatetags.static import static

from vue_helper.dist import vue_dist_css, vue_dist_js


def set_production_assets_paths(vue_dist_path):
    try:
        with open(os.path.join(vue_dist_path, 'index.html'), 'r') as index_file:
            js, css = get_js_and_css_links_from_html(index_file.read())
            vue_dist_js.update(js)
            vue_dist_css.update(css)
    except FileNotFoundError as err:
        logging.warning(f'Vue dist index.html is not found at {vue_dist_path}')


def get_js_and_css_links_from_html(html: str) -> tuple:
    """
    Parse HTML document and return a tuple of javascript and css links.
    """
    js = set([alias_path(match) for match in
              re.findall(r'<script src=[\"]?(\S+.js)', html, re.IGNORECASE)])
    css = set([alias_path(match) for match in
               re.findall(r'<link href=[\"]?(\S+.css)', html, re.IGNORECASE)])
    return js, css


def alias_path(path):
    return static(f'{settings.VUE_APP_DIST_DIR_NAME}{path}')
