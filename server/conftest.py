import sys
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.config.settings'

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


def pytest_configure():
    django.setup()
    sys.path.append(os.path.join(PROJECT_ROOT, 'server/apps'))
