from django.contrib import admin

from solo.admin import SingletonModelAdmin
from core import models


admin.site.register(models.Settings, SingletonModelAdmin)
