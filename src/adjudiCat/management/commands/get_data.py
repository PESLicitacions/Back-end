from publicdata.views import get_data
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'adjudiCat.settings.common.py'
django.setup()

get_data()
