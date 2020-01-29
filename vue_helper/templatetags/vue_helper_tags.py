from django import template
from django.conf import settings

from vue_helper.dist import vue_dist_js, vue_dist_css

register = template.Library()


@register.inclusion_tag('vue_helper/vue_scripts.html')
def vue_scripts():
    return {
        'VUE_DEV_MODE': settings.VUE_DEV_MODE,
        'VUE_DEV_SERVER_URL': settings.VUE_DEV_SERVER_URL,
        'VUE_DIST_JS': vue_dist_js
    }


@register.inclusion_tag('vue_helper/vue_preload_scripts.html')
def vue_preload_scripts():
    return {
        'VUE_DEV_MODE': settings.VUE_DEV_MODE,
        'VUE_DIST_JS': vue_dist_js
    }


@register.inclusion_tag('vue_helper/vue_styles.html')
def vue_styles():
    return {
        'VUE_DEV_MODE': settings.VUE_DEV_MODE,
        'VUE_DEV_SERVER_URL': settings.VUE_DEV_SERVER_URL,
        'VUE_DIST_CSS': vue_dist_css
    }


@register.inclusion_tag('vue_helper/vue_preload_styles.html')
def vue_preload_styles():
    return {
        'VUE_DEV_MODE': settings.VUE_DEV_MODE,
        'VUE_DIST_CSS': vue_dist_css
    }
