# from suit.apps import DjangoSuitConfig
from django.apps import AppConfig

class MakeupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'makeup'




# class SuitConfig(DjangoSuitConfig):
#     """ change desgin of admen panal use library  django-suit """
#     layout = 'horizontal'