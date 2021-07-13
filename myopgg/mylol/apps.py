from django.apps import AppConfig

# 해당 application의 이름과 별칭을 정할 수 있는 code입니다

class MylolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mylol'

class LoLConfig(AppConfig):
    name = 'myopgg.mylol'