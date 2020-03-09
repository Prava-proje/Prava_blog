from django.contrib import admin

from core import models

admin.site.register(models.HeaderCategory)
admin.site.register(models.WebsiteSetting)
admin.site.register(models.TestCategory)
admin.site.register(models.QuestionAnswer)