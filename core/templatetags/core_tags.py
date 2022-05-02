import html
import json

from django import template
from django.template import Template, Context

from pwa import app_settings


register = template.Library()


@register.inclusion_tag('pwa.html', takes_context=True)
def pwa(context):
    manifest_data = {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    }

    manifest_data['PWA_APP_ICONS'] = json.loads(
        Template(
            '{% load static %}' + html.unescape(json.dumps(manifest_data['PWA_APP_ICONS']))
        ).render(Context())
    )

    return manifest_data
