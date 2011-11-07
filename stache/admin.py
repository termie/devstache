
from django.contrib import admin

from stache import models


class ResultAdmin(admin.ModelAdmin):
  pass

admin.site.register(models.Result, ResultAdmin)


class ArchAdmin(admin.ModelAdmin):
  pass

admin.site.register(models.Arch, ArchAdmin)


class VersionAdmin(admin.ModelAdmin):
  pass

admin.site.register(models.Version, VersionAdmin)
