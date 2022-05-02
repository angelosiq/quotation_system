import json
import html

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.generic import TemplateView

from pwa import views as pwa_views


class Main(TemplateView):
    template_name = "core/main.html"


def offline(request):
    return render(request, "offline.html")


def favicon_ico(request):
    with open(staticfiles_storage.path("images/icons/icon-72x72.png"), 'rb') as ico:
        return HttpResponse(content=ico.read(), content_type='image/png')


def service_worker(request):
    with open(settings.PWA_SERVICE_WORKER_PATH, 'r') as service_worker_file:
        response = HttpResponse(
            Template(service_worker_file.read()).render(Context({})),
            content_type='application/javascript'
        )
    return response


def manifest(request):
    app_settings = pwa_views.app_settings
    manifest_data = {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    }

    manifest_with_rendered_statics = Template(
        '{% load static %}' + html.unescape(render_to_string('core/manifest.json', manifest_data))
    ).render(Context())

    manifest_json = json.loads(manifest_with_rendered_statics)
    manifest_json['prefer_related_applications'] = False

    return JsonResponse(manifest_json)
