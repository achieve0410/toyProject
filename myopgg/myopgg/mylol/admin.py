from django.contrib import admin
from . import models

# Register your models here.
# 관리자 페이지에서 해당 application을 다루기 위한 code입니다

@admin.register(models.Riot)
class RiotAdmin(admin.ModelAdmin):

    search_fields = (
        'api_key',
    )