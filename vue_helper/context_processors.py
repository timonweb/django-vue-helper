from django.conf import settings


def vue_dev_mode(request):
    return {
        'VUE_DEV_MODE': settings.VUE_DEV_MODE
    }
