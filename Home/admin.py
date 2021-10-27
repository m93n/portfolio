from django.contrib import admin
from . import models

class SkillAdmin(admin.ModelAdmin):
    fields = ('name', 'duration')

admin.site.register(models.home_page)
admin.site.register(models.media_page)
admin.site.register(models.contact)
admin.site.register(models.contactLink)
admin.site.register(models.about)
admin.site.register(models.skill, SkillAdmin)
admin.site.register(models.workExp)
admin.site.register(models.educationExp)
